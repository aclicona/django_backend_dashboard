import { GraphQLClient } from 'graphql-request'

const endpoint = 'http://127.0.0.1:8000/graphql'

const graphqlClient = new GraphQLClient(endpoint)
export { graphqlClient }

export default {
  install: function(app) {
    app.provide('graphql', graphqlClient)
  }
}
