<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navigation -->
    <nav class="bg-white shadow-lg">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <h1 class="text-xl font-semibold text-gray-900">Welcome to your Bank!</h1>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/dashboard" class="text-gray-900 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
              Dashboard
            </router-link>
            <router-link to="/accounts" class="text-gray-500 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
              Accounts
            </router-link>
            <router-link to="/transactions" class="text-gray-500 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
              Transactions
            </router-link>
            <router-link to="/transfer" class="text-gray-500 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
              Transfer
            </router-link>
            <button @click="logout" class="text-gray-500 hover:text-red-600 px-3 py-2 rounded-md text-sm font-medium">
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div v-if="loading" class="text-center">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
        <p class="mt-2 text-gray-600">Loading dashboard...</p>
      </div>

      <div v-else-if="error" class="text-center text-red-600">
        {{ error }}
      </div>

      <div v-else class="px-4 py-6 sm:px-0">
        <!-- Welcome Section -->
        <div class="bg-white overflow-hidden shadow rounded-lg mb-6">
          <div class="px-4 py-5 sm:p-6">
            <h2 class="text-lg font-medium text-gray-900 mb-2">
              Welcome back, {{ dashboardData.user.full_name }}!
            </h2>
            <p class="text-sm text-gray-600">
              Account created: {{ formatDate(dashboardData.user.created_at) }}
            </p>
          </div>
        </div>

        <!-- Account Summary Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <dt class="text-sm font-medium text-gray-500 truncate">Total Balance</dt>
              <dd class="mt-1 text-3xl font-semibold text-gray-900">
                ${{ formatCurrency(dashboardData.total_balance) }}
              </dd>
            </div>
          </div>
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <dt class="text-sm font-medium text-gray-500 truncate">Total Accounts</dt>
              <dd class="mt-1 text-3xl font-semibold text-gray-900">
                {{ dashboardData.accounts.length }}
              </dd>
            </div>
          </div>
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <dt class="text-sm font-medium text-gray-500 truncate">Recent Transactions</dt>
              <dd class="mt-1 text-3xl font-semibold text-gray-900">
                {{ dashboardData.recent_transactions.length }}
              </dd>
            </div>
          </div>
        </div>

        <!-- Account Summary -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">
          <div 
            v-for="account in dashboardData.accounts" 
            :key="account.id"
            class="bg-white overflow-hidden shadow rounded-lg"
          >
            <div class="px-4 py-5 sm:p-6">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <div class="w-8 h-8 bg-indigo-500 rounded-full flex items-center justify-center">
                    <span class="text-white text-sm font-medium">{{ account.account_type.charAt(0).toUpperCase() }}</span>
                  </div>
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">
                      {{ account.account_type }} Account
                    </dt>
                    <dd class="text-lg font-medium text-gray-900">
                      ${{ formatCurrency(account.balance) }}
                    </dd>
                    <dd class="text-sm text-gray-500">
                      {{ account.account_number }}
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Recent Transactions -->
        <div class="bg-white shadow overflow-hidden sm:rounded-md">
          <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">Recent Transactions</h3>
            <p class="mt-1 max-w-2xl text-sm text-gray-500">Your latest account activity</p>
          </div>
          <ul class="divide-y divide-gray-200">
            <li v-for="transaction in dashboardData.recent_transactions" :key="transaction.id" class="px-4 py-4 sm:px-6">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <div class="flex-shrink-0">
                    <div 
                      :class="[
                        'w-8 h-8 rounded-full flex items-center justify-center',
                        transaction.transaction_type === 'deposit' ? 'bg-green-100' : 
                        transaction.transaction_type === 'withdrawal' ? 'bg-red-100' : 'bg-blue-100'
                      ]"
                    >
                      <span 
                        :class="[
                          'text-sm font-medium',
                          transaction.transaction_type === 'deposit' ? 'text-green-800' : 
                          transaction.transaction_type === 'withdrawal' ? 'text-red-800' : 'text-blue-800'
                        ]"
                      >
                        {{ transaction.transaction_type.charAt(0).toUpperCase() }}
                      </span>
                    </div>
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">
                      {{ transaction.description || transaction.transaction_type }}
                    </div>
                    <div class="text-sm text-gray-500">
                      {{ formatDate(transaction.created_at) }}
                      <span v-if="transaction.sender_username || transaction.receiver_username">
                        • {{ transaction.sender_username === dashboardData.user.username ? 'To: ' + transaction.receiver_username : 'From: ' + transaction.sender_username }}
                      </span>
                    </div>
                  </div>
                </div>
                <div class="text-sm font-medium" :class="getTransactionAmountClass(transaction)">
                  {{ getTransactionAmountDisplay(transaction) }}
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
// import api from '../services/api' // TODO: Uncomment when API is ready

export default {
  name: 'Dashboard',
  data() {
    return {
      dashboardData: {
        user: {
          full_name: 'Antonio Demo',
          username: 'tonio_user',
          created_at: '2024-01-15T10:30:00Z'
        },
        accounts: [
          {
            id: 1,
            account_number: 'ACC001234567',
            account_type: 'checking',
            balance: 2500.75,
            currency: 'USD',
            is_active: true
          },
          {
            id: 2,
            account_number: 'ACC001234568',
            account_type: 'savings',
            balance: 15000.00,
            currency: 'USD',
            is_active: true
          },
          {
            id: 3,
            account_number: 'ACC001234569',
            account_type: 'credit',
            balance: -850.25,
            currency: 'USD',
            is_active: true
          }
        ],
        recent_transactions: [
          {
            id: 1,
            transaction_id: 'TXN001',
            transaction_type: 'deposit',
            amount: 1000.00,
            description: 'Salary Deposit',
            status: 'completed',
            created_at: '2024-07-10T14:30:00Z',
            sender_username: null,
            receiver_username: 'tonio_user'
          },
          {
            id: 2,
            transaction_id: 'TXN002',
            transaction_type: 'withdrawal',
            amount: 150.00,
            description: 'ATM Withdrawal',
            status: 'completed',
            created_at: '2024-07-09T16:45:00Z',
            sender_username: 'tonio_user',
            receiver_username: null
          },
          {
            id: 3,
            transaction_id: 'TXN003',
            transaction_type: 'transfer',
            amount: 300.00,
            description: 'Transfer to John Doe',
            status: 'completed',
            created_at: '2024-07-08T11:20:00Z',
            sender_username: 'tonio_user',
            receiver_username: 'john_doe'
          },
          {
            id: 4,
            transaction_id: 'TXN004',
            transaction_type: 'deposit',
            amount: 50.00,
            description: 'Interest Payment',
            status: 'completed',
            created_at: '2024-07-07T09:00:00Z',
            sender_username: null,
            receiver_username: 'tonio_user'
          }
        ],
        total_balance: 16650.50
      },
      loading: false,
      error: null
    }
  },
  mounted() {
    // Simulate loading for demo purposes
    this.simulateLoading()
  },
  methods: {
    simulateLoading() {
      this.loading = true
      setTimeout(() => {
        this.loading = false
      }, 1000)
    },
    logout() {
      // Remove token and redirect to login
      localStorage.removeItem('token')
      this.$router.push('/login')
    },
    formatCurrency(amount) {
      return parseFloat(amount).toFixed(2)
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString()
    },
    getTransactionAmountClass(transaction) {
      if (transaction.transaction_type === 'deposit') {
        return 'text-green-600'
      } else if (transaction.transaction_type === 'withdrawal') {
        return 'text-red-600'
      } else if (transaction.transaction_type === 'transfer') {
        return transaction.sender_username === this.dashboardData.user.username ? 'text-red-600' : 'text-green-600'
      }
      return 'text-gray-900'
    },
    getTransactionAmountDisplay(transaction) {
      const amount = this.formatCurrency(transaction.amount)
      if (transaction.transaction_type === 'deposit') {
        return `+$${amount}`
      } else if (transaction.transaction_type === 'withdrawal') {
        return `-$${amount}`
      } else if (transaction.transaction_type === 'transfer') {
        return transaction.sender_username === this.dashboardData.user.username ? `-$${amount}` : `+$${amount}`
      }
      return `$${amount}`
    }
  }
}
</script>
