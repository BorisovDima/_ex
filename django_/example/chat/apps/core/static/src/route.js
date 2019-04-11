import Vue from 'vue'
import Router from 'vue-router'

import Home from './home.vue'
import Login from './login.vue'
import User from './user.vue'
import Room from './room.vue'
import Message from './message.vue'

import auth from './utils/auth.js'

import ws from './utils/ws.js'

ws.connect()
auth.checkAuth()

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/user/:id',
            name: 'user',
            component: User
        },
    ]
})
