# Bank API

A full-stack banking application built with FastAPI (Python) backend and Vue.js frontend with Tailwind CSS.

## Project Structure

```
bank-api/
├── backend/                 # FastAPI Python backend
│   ├── app/
│   │   ├── main.py         # FastAPI application entry point
│   │   ├── api/            # API route handlers
│   │   │   ├── accounts.py
│   │   │   ├── auth.py
│   │   │   └── users.py
│   │   ├── core/
│   │   │   └── config.py   # Configuration settings
│   │   ├── database/
│   │   │   └── database.py # Database connection
│   │   ├── models/
│   │   │   └── models.py   # Database models
│   │   ├── schemas/
│   │   │   └── schemas.py  # Pydantic schemas
│   │   └── services/       # Business logic
│   ├── tests/              # Backend tests
│   └── requirements.txt    # Python dependencies
└── frontend/               # Vue.js frontend
    ├── src/
    │   ├── views/
    │   │   ├── Login.vue   # Login/Registration page
    │   │   └── Dashboard.vue # User dashboard
    │   ├── router/
    │   │   └── index.js    # Vue Router configuration
    │   ├── services/
    │   │   └── api.js      # API service layer
    │   └── assets/         # CSS and static assets
    ├── package.json        # Node.js dependencies
    └── vite.config.ts      # Vite configuration
```

## Features

### Backend (FastAPI)
- User authentication and authorization
- Account management
- Transaction processing
- RESTful API endpoints
- Database integration
- Input validation with Pydantic

### Frontend (Vue.js)
- User login and registration
- Responsive dashboard
- Account overview
- Transaction history
- Modern UI with Tailwind CSS v4
- Single Page Application (SPA)
- Protected routes with authentication guards

## Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Python 3.x** - Programming language
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vue Router** - Official router for Vue.js
- **Tailwind CSS v4** - Utility-first CSS framework
- **Vite** - Fast build tool and development server
- **Axios** - HTTP client for API requests
- **TypeScript** - Type-safe JavaScript

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## API Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/register` - User registration
- `POST /auth/logout` - User logout

### Users
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile

### Accounts
- `GET /accounts` - Get user accounts
- `POST /accounts` - Create new account
- `GET /accounts/{id}` - Get specific account

### Transactions
- `GET /transactions` - Get user transactions
- `POST /transactions` - Create new transaction

## Development

### Backend Development
- The FastAPI server runs with hot reload using `--reload` flag
- API documentation is automatically generated at `/docs`
- Database models are defined in `models/models.py`
- API schemas are defined in `schemas/schemas.py`

### Frontend Development
- Vite provides hot module replacement for fast development
- Vue components are organized by feature
- Tailwind CSS utilities are available throughout the application
- API calls are centralized in `services/api.js`

## Building for Production

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm run build
npm run preview
```

## Authentication Flow

1. User submits login credentials
2. Backend validates credentials and returns JWT token
3. Frontend stores token in localStorage
4. Protected routes check for valid token
5. API requests include token in Authorization header

## Database Schema

The application uses a relational database with the following main entities:
- Users (authentication and profile information)
- Accounts (bank accounts belonging to users)
- Transactions (financial transactions between accounts)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is for educational purposes.
