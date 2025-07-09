import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor to handle token expiration
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default {
  // Auth endpoints
  login(credentials) {
    const formData = new FormData()
    formData.append('username', credentials.username)
    formData.append('password', credentials.password)
    
    return api.post('/api/auth/token', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
  },

  register(userData) {
    return api.post('/api/auth/register', userData)
  },

  getCurrentUser() {
    return api.get('/api/auth/me')
  },

  // User endpoints
  getDashboard() {
    return api.get('/api/users/dashboard')
  },

  getUsers() {
    return api.get('/api/users/')
  },

  // Account endpoints
  getAccounts() {
    return api.get('/api/accounts/')
  },

  createAccount(accountData) {
    return api.post('/api/accounts/', accountData)
  },

  getAccount(accountId) {
    return api.get(`/api/accounts/${accountId}`)
  },

  // Transaction endpoints
  getTransactions() {
    return api.get('/api/transactions/')
  },

  createTransaction(transactionData) {
    return api.post('/api/transactions/', transactionData)
  },

  getTransaction(transactionId) {
    return api.get(`/api/transactions/${transactionId}`)
  },

  // Card endpoints
  getCards() {
    return api.get('/api/cards/')
  },

  createCard(cardData) {
    return api.post('/api/cards/', cardData)
  },
}
