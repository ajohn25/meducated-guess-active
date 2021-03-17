import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/pages/Login'
import CreateAccount from '@/pages/CreateAccount'
import HomeScreen from '@/pages/HomeScreen'
import Chatbot from '@/pages/Chatbot'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', name: 'login', component: Login },
    { path: '/createAccount', name: 'Create Account', component: CreateAccount },
    { path: '/homescreen', name: 'Home Screen', component: HomeScreen },
    { path: '/chatbot', name: 'Chatbot', component: Chatbot }
  ]
})
