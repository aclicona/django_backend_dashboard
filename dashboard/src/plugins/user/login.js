import { LOGIN, ME_USER } from '@/graph/user.js'
import { graphqlClient } from '../graphql'

const loginUser = async (credentials) => {
  try {
    const { loginAuthToken } = await graphqlClient.request(LOGIN, credentials)
    console.log(loginAuthToken)
    if (loginAuthToken.success && loginAuthToken.user.isActive && loginAuthToken.user.isStaff) {
      console.log('True')
      return true
    }
  } catch (e) {
    console.error(e)
    return false
  }
}
const userIsLoggedIn = async () => {
  try {
    const { me } = await graphqlClient.request(ME_USER)
    console.log(me)
    return !!me

  } catch (e) {
    console.error(e)
    return false
  }
}


export default {
  install: async function(app) {
    const userLogin = {
      async login(credentials) {
        return await loginUser(credentials)
      },
      async isLogged() {
        return await userIsLoggedIn()
      }
    }
    app.provide('userLogin', userLogin)
  }
}