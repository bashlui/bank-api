<template>
  <div class="min-h-screen w-full flex items-center justify-center bg-gradient-to-br from-pink-400 via-purple-500 to-fuchsia-700 p-4">
    <div class="w-full max-w-md mx-auto">
      <!-- Header Section -->
      <div class="text-center mb-8">
        <h2 class="text-3xl font-extrabold text-white mb-2">
          Sign in to your account
        </h2>
        <p class="text-sm text-white/80">
          Welcome to Bank API
        </p>
      </div>

      <!-- Login Form -->
      <div class="bg-white/10 backdrop-blur-md rounded-xl p-8 shadow-xl">
        <form class="space-y-6" @submit.prevent="handleLogin">
          <!-- Input Fields -->
          <div class="space-y-4">
            <div>
              <label for="username" class="block text-sm font-medium text-white mb-2">
                Username
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                v-model="form.username"
                class="w-full px-4 py-3 bg-white/20 border border-white/30 rounded-lg text-white placeholder-white/60 focus:outline-none focus:ring-2 focus:ring-white/50 focus:border-transparent transition-all duration-200"
                placeholder="Enter your username"
              />
            </div>
            
            <div>
              <label for="password" class="block text-sm font-medium text-white mb-2">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                v-model="form.password"
                class="w-full px-4 py-3 bg-white/20 border border-white/30 rounded-lg text-white placeholder-white/60 focus:outline-none focus:ring-2 focus:ring-white/50 focus:border-transparent transition-all duration-200"
                placeholder="Enter your password"
              />
            </div>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="bg-red-500/20 border border-red-500/30 text-red-100 text-sm p-3 rounded-lg">
            {{ error }}
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full py-3 px-4 bg-white text-purple-600 font-semibold rounded-lg hover:bg-white/90 focus:outline-none focus:ring-2 focus:ring-white/50 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02]"
          >
            <span v-if="loading" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-purple-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Signing in...
            </span>
            <span v-else>Sign in</span>
          </button>

          <!-- Sign up link -->
          <div class="text-center pt-4">
            <router-link 
              to="/register" 
              class="text-white/80 hover:text-white text-sm font-medium transition-colors duration-200 underline underline-offset-2"
            >
              Don't have an account? Sign up
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      loading: false,
      error: null
    }
  },
  methods: {
    async handleLogin() {
      this.loading = true
      this.error = null

      try {
        const response = await api.login(this.form)
        localStorage.setItem('token', response.data.access_token)
        this.$router.push('/dashboard')
      } catch (error) {
        this.error = error.response?.data?.detail || 'Login failed'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
