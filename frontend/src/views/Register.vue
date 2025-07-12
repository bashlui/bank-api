<template>
  <div
    class="min-h-screen w-full flex items-center justify-center bg-gradient-to-br from-[#0f0c29] via-[#302b63] to-[#24243e] p-4"
  >
    <div class="w-full max-w-md mx-auto">
      <!-- Registration Form -->
      <div class="bg-white/10 backdrop-blur-md rounded-xl p-8 shadow-xl">
        <!-- Header Section -->
        <div class="text-center mb-8">
          <h2 class="text-3xl font-extrabold text-white mb-2">Create an account</h2>
          <p class="text-sm text-white/80">Made by Tonio</p>
        </div>
        <form class="space-y-6" @submit.prevent="handleRegister">
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
              <label for="email" class="block text-sm font-medium text-white mb-2">
                Email
              </label>
              <input
                id="email"
                name="email"
                type="email"
                required
                v-model="form.email"
                class="w-full px-4 py-3 bg-white/20 border border-white/30 rounded-lg text-white placeholder-white/60 focus:outline-none focus:ring-2 focus:ring-white/50 focus:border-transparent transition-all duration-200"
                placeholder="Enter your email"
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
          <div
            v-if="error"
            class="bg-red-500/20 border border-red-500/30 text-red-100 text-sm p-3 rounded-lg"
          >
            {{ error }}
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full py-3 px-4 bg-white text-gray-900 font-semibold rounded-lg hover:bg-white/90 focus:outline-none focus:ring-2 focus:ring-white/50 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02]"
          >
            <span v-if="loading" class="flex items-center justify-center">
              <svg
                class="animate-spin -ml-1 mr-3 h-5 w-5 text-purple-600"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  class="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
                ></circle>
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              Signing up...
            </span>
            <span v-else>Sign up</span>
          </button>

          <!-- Sign in link -->
          <div class="text-center pt-4">
            <router-link
              to="/login"
              class="text-white/80 hover:text-white text-sm font-medium transition-colors duration-200 underline underline-offset-2"
            >
              Already have an account? Sign in
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// import api from '../services/api' // TODO: Uncomment when ready to handle API validations

export default {
  name: 'Register',
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
      },
      loading: false,
      error: null,
    }
  },
  methods: {
    async handleRegister() {
      this.loading = true
      this.error = null

      // TODO: Add API validation later
      // Simulate loading for now
      setTimeout(() => {
        this.loading = false
        // For now, just redirect to login without API call
        this.$router.push('/login')
      }, 1000)
    },
  },
}
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
