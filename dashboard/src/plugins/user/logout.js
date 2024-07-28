import { LOGOUT } from '@/graph/user.js';
import { graphqlClient } from '../graphql'

const logoutUser = async () => {
    try {
        const {logoutUser}= await graphqlClient.request(LOGOUT, {})
        return logoutUser.logout
    } catch (e) {
        console.error(e)
    }
}

export default {
  install: async function(app) {
    app.provide('logoutUser', logoutUser)
  }
}