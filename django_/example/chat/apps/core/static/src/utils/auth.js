import ws from './ws.js'


export default {

  LOGIN_URL: 'http://localhost:8000/auth/o/vk-oauth2/',
  REDIRCT_URL: 'http://localhost:8080/',

  user: {
    authenticated: false
  },
  get_redirect(){
    $.ajax({
      url: this.LOGIN_URL,
      method: 'GET',
      data: {'redirect_uri': this.REDIRCT_URL},
      success: function(data) {
         console.log(data)
         window.location = data['authorization_url']
      }

    })
},
//     ws.send({
//         url: this.LOGIN_URL,
//         method: 'GET',
//         params: {'redirect_uri': this.REDIRCT_URL},
//         callback: function(data) {
//            window.location = data['authorization_url']
//         }
//     })
  // login(context, creds, redirect) {
  //   context.$http.post(LOGIN_URL, creds, (data) => {
  //     localStorage.setItem('id_token', data.id_token)
  //     localStorage.setItem('access_token', data.access_token)
  //
  //     this.user.authenticated = true
  //
  //     // Redirect to a specified route
  //     if(redirect) {
  //       router.go(redirect)
  //     }
  //
  //   }).error((err) => {
  //     context.error = err
  //   })
  // },

  // signup(context, creds, redirect) {
  //   context.$http.post(SIGNUP_URL, creds, (data) => {
  //     localStorage.setItem('id_token', data.id_token)
  //     localStorage.setItem('access_token', data.access_token)
  //
  //     this.user.authenticated = true
  //
  //     if(redirect) {
  //       router.go(redirect)
  //     }
  //
  //   }).error((err) => {
  //     context.error = err
  //   })
  // },

  // To log out, we just need to remove the token
  logout() {
    localStorage.removeItem('id_token')
    localStorage.removeItem('access_token')
    this.user.authenticated = false
  },

  checkAuth() {
    var jwt = localStorage.getItem('id_token')
    console.log(jwt)
    if(jwt) {
      this.user.authenticated = true
    }
    else {
      this.user.authenticated = false
    }
    var params = new URLSearchParams(window.location.search)
    var state = params.get('state')
    var code = params.get('code')
    var redirect_state = params.get('redirect_state')
    console.log(code, state, 'AUTHHHHH')
    if (state || code || redirect_state){
      //      ws.send({
      //          url: this.LOGIN_URL,
      //          method: 'POST',
      //          data: {'code': code, 'state': state, 'redirect_state': redirect_state},
      //          callback: function(data) {
      //            console.log(data)
      //
      //          }
      //      })
                 $.ajax({
              url: this.LOGIN_URL,
              method: 'POST',
              data: {'code': code, 'state': state, 'redirect_state': redirect_state},
              success: function(data) {
                 console.log(data)

              }

            })
    }
  },

  // The object to be passed as a header for authenticated requests
  getAuthHeader() {
    return {
      'Authorization': 'Bearer ' + localStorage.getItem('access_token')
    }
  }
}
