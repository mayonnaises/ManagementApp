import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/edit',
    name: 'Edit',
    component: () => import('../views/Edit.vue')
  },
  {
    path: '/list',
    name: 'List',
    component: () => import('../views/List.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
