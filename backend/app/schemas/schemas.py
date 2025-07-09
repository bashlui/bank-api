from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from enum import Enum

class TransactionStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TransactionType(str, Enum):
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    PAYMENT = "payment"

class CardType(str, Enum):
    DEBIT = "debit"
    CREDIT = "credit"

# User schemas
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    full_name: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

# Account schemas
class AccountCreate(BaseModel):
    account_type: str = Field(..., description="Type of account (checking, savings)")
    initial_balance: Optional[Decimal] = Field(default=0.00, description="Initial balance")

class AccountResponse(BaseModel):
    id: int
    account_number: str
    account_type: str
    balance: Decimal
    currency: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Card schemas
class CardCreate(BaseModel):
    card_holder_name: str
    card_type: CardType
    account_id: int

class CardResponse(BaseModel):
    id: int
    card_number: str
    card_holder_name: str
    card_type: CardType
    expiry_month: int
    expiry_year: int
    masked_card_number: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Transaction schemas
class TransactionCreate(BaseModel):
    amount: Decimal = Field(..., gt=0, description="Transaction amount")
    currency: str = Field(default="USD", description="Currency code")
    transaction_type: TransactionType
    description: Optional[str] = None
    reference: Optional[str] = None
    receiver_username: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    transaction_id: str
    amount: Decimal
    currency: str
    transaction_type: TransactionType
    status: TransactionStatus
    description: Optional[str]
    reference: Optional[str]
    created_at: datetime
    sender_username: Optional[str]
    receiver_username: Optional[str]
    
    class Config:
        from_attributes = True

# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Dashboard schemas
class DashboardResponse(BaseModel):
    user: UserResponse
    accounts: List[AccountResponse]
    recent_transactions: List[TransactionResponse]
    total_balance: Decimal
