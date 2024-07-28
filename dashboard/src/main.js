import './assets/main.css'

import App from './App.vue'
import router from './router'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import graphql from '@/plugins/graphql.js'
// import { pluginformatDate } from '@/plugins/format-value.js'
import userLogin from '@/plugins/user/login.js'
import logoutUser from '@/plugins/user/logout.js'
import vClickOutside from "click-outside-vue3"

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(graphql)
// app.use(pluginformatDate)
app.use(userLogin)
app.use(logoutUser)
app.use(vClickOutside)
app.mount('#app')
