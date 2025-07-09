<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navigation -->
    <nav class="bg-white shadow-lg">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <h1 class="text-xl font-semibold text-gray-900">Bank API</h1>
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

        <!-- Accounts Overview -->
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

        <!-- Accounts List -->
        <div class="bg-white shadow overflow-hidden sm:rounded-md mb-6">
          <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">Your Accounts</h3>
            <p class="mt-1 max-w-2xl text-sm text-gray-500">Manage your bank accounts</p>
          </div>
          <ul class="divide-y divide-gray-200">
            <li v-for="account in dashboardData.accounts" :key="account.id" class="px-4 py-4 sm:px-6">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm font-medium text-gray-900">
                    {{ account.account_number }}
                  </p>
                  <p class="text-sm text-gray-500">
                    {{ account.account_type }} • {{ account.currency }}
                  </p>
                </div>
                <div class="text-right">
                  <p class="text-sm font-medium text-gray-900">
                    ${{ formatCurrency(account.balance) }}
                  </p>
                  <p class="text-sm text-gray-500">
                    {{ account.is_active ? 'Active' : 'Inactive' }}
                  </p>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <!-- Recent Transactions -->
        <div class="bg-white shadow overflow-hidden sm:rounded-md">
          <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">Recent Transactions</h3>
            <p class="mt-1 max-w-2xl text-sm text-gray-500">Your latest transaction history</p>
          </div>
          <ul class="divide-y divide-gray-200">
            <li v-for="transaction in dashboardData.recent_transactions" :key="transaction.id" class="px-4 py-4 sm:px-6">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm font-medium text-gray-900">
                    {{ transaction.transaction_id }}
                  </p>
                  <p class="text-sm text-gray-500">
                    {{ transaction.transaction_type }} • {{ transaction.status }}
                  </p>
                  <p v-if="transaction.description" class="text-sm text-gray-500">
                    {{ transaction.description }}
                  </p>
                </div>
                <div class="text-right">
                  <p class="text-sm font-medium" :class="getTransactionAmountClass(transaction)">
                    {{ getTransactionAmountDisplay(transaction) }}
                  </p>
                  <p class="text-sm text-gray-500">
                    {{ formatDate(transaction.created_at) }}
                  </p>
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
import api from '../services/api'

export default {
  name: 'Dashboard',
  data() {
    return {
      dashboardData: null,
      loading: true,
      error: null
    }
  },
  async mounted() {
    await this.fetchDashboardData()
  },
  methods: {
    async fetchDashboardData() {
      this.loading = true
      this.error = null

      try {
        const response = await api.getDashboard()
        this.dashboardData = response.data
      } catch (error) {
        this.error = error.response?.data?.detail || 'Failed to load dashboard'
      } finally {
        this.loading = false
      }
    },
    logout() {
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
