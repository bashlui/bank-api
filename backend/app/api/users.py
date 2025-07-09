from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.models import User
from app.schemas.schemas import UserResponse, DashboardResponse
from app.api.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/dashboard", response_model=DashboardResponse)
async def get_dashboard(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    from app.models.models import Account, Transaction
    from decimal import Decimal
    
    # Get user's accounts
    accounts = db.query(Account).filter(Account.user_id == current_user.id).all()
    
    # Get recent transactions
    recent_transactions = db.query(Transaction).filter(
        (Transaction.sender_id == current_user.id) | (Transaction.receiver_id == current_user.id)
    ).order_by(Transaction.created_at.desc()).limit(10).all()
    
    # Calculate total balance
    total_balance = sum(account.balance for account in accounts)
    
    # Format transaction responses
    transaction_responses = []
    for transaction in recent_transactions:
        sender_user = db.query(User).filter(User.id == transaction.sender_id).first()
        receiver_user = db.query(User).filter(User.id == transaction.receiver_id).first()
        
        transaction_responses.append({
            "id": transaction.id,
            "transaction_id": transaction.transaction_id,
            "amount": transaction.amount,
            "currency": transaction.currency,
            "transaction_type": transaction.transaction_type,
            "status": transaction.status,
            "description": transaction.description,
            "reference": transaction.reference,
            "created_at": transaction.created_at,
            "sender_username": sender_user.username if sender_user else None,
            "receiver_username": receiver_user.username if receiver_user else None,
        })
    
    return {
        "user": current_user,
        "accounts": accounts,
        "recent_transactions": transaction_responses,
        "total_balance": total_balance
    }
