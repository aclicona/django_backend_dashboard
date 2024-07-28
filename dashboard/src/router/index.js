import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import {auth} from "../middleware/auth"
import DashBoard from '@/components/DashBoard.vue'
import HomeView from '@/views/HomeView.vue'

const routes = [
  { path: '/', redirect: { name: 'home' } },
  { path: '/login', name: 'login', component: LoginView },
  // { path: '/cuenta/password-reset/:token', name: 'passwordReset', component: PasswordReset, props: true },
  {
    path: '/dashboard', component: DashBoard, children: [
      { path: '/', redirect: { name: 'home' } },
      { path: 'home', name: 'home', component: HomeView },
      // {
      //   path: '/about',
      //   name: 'about',
      //   // route level code-splitting
      //   // this generates a separate chunk (About.[hash].js) for this route
      //   // which is lazy-loaded when the route is visited.
      //   component: () => import('../views/AboutView.vue')
      // }

    ],
    meta: {
      middleware: auth
    }
  }
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

// Creates a `nextMiddleware()` function which not only
// runs the default `next()` callback but also triggers
// the subsequent Middleware function.
// function nextFactory(context, middleware, index) {
//   const subsequentMiddleware = middleware[index]
//   // If no subsequent Middleware exists,
//   // the default `next()` callback is returned.
//   if (!subsequentMiddleware) return context.next
//
//   return (...parameters) => {
//     // Run the default Vue Router `next()` callback first.
//     context.next(...parameters)
//     // Then run the subsequent Middleware with a new
//     // `nextMiddleware()` callback.
//     const nextMiddleware = nextFactory(context, middleware, index + 1)
//     subsequentMiddleware({ ...context, next: nextMiddleware })
//   }
// }
//
// router.beforeEach((to, from, next) => {
//   if (to.meta.middleware) {
//     const middleware = Array.isArray(to.meta.middleware)
//       ? to.meta.middleware
//       : [to.meta.middleware]
//
//     const context = {
//       from,
//       next,
//       router,
//       to
//     }
//     const nextMiddleware = nextFactory(context, middleware, 1)
//     return middleware[0]({ ...context, next: nextMiddleware })
//   }
//   return next()
// })

export default router
