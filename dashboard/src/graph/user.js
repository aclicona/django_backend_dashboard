import gql from 'graphql-tag'


const LOGOUT = gql`mutation logoutUser{
  logoutUser{
    logout
  }
}`

const LOGIN = gql`
  mutation loginAuthToken($email: String!, $password: String!){
    loginAuthToken(email:$email, password: $password){
    success
    errors
    token {
      token
    }
    refreshToken{
      token
    }
    user {
      email
      isStaff
      isActive
    }
  }
}
`
const CREATE_USER = gql`
  mutation createStaffUser($email: String!, $firstName: String!, $lastName: String!, $groups:JSONString!){
    createStaffUser(email:$email, firstName: $firstName, lastName: $lastName, groups: $groups){
    success
  }
}
`
const ME_USER = gql`
        query {
          me{
            id
            email
            firstName
            lastName
            image  
          }
        }
      `
const UPDATE_USER = gql`
      mutation updateUserInfo($firstName: String, $lastName: String, $avatar: Upload){
        updateUserInfo(firstName:$firstName, lastName:$lastName, avatar: $avatar){
          success
        }
      }
      `
const GET_USER_GROUPS = gql`
        query {
          gruposUsuarios
        }
      `
const PASSWORD_RESET = `
      mutation passwordReset($token: String!, $password:String!){
            passwordReset(token: $token, newPassword1: $password, newPassword2: $password) {
                  success,
                  errors
            }
      }
`
export { LOGIN, ME_USER, LOGOUT, UPDATE_USER, CREATE_USER, GET_USER_GROUPS, PASSWORD_RESET }