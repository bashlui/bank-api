import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue' // Import Dashboard component

const routes = [
  {
    path: '/',
    redirect: '/dashboard'  // Skip login, go directly to dashboard
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard for authentication - TODO: Uncomment when authentication is ready
/*
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!token) {
      next('/login')
    } else {
      next()
    }
  } else {
    if (token && to.path === '/login') {
      next('/dashboard')
    } else {
      next()
    }
  }
})
*/

export default router
