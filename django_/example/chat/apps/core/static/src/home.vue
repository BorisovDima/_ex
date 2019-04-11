<template>
  <div>

<div v-if="auth">
OK
</div>

<div v-else>

  <Login>

    
  </Login>

</div>



<button @click="$router.push('/login')">/login</button>
  </div>
</template>


<script>
import room from './room.vue'
import login from './login.vue'
import auth from './utils/auth.js'



export default {
  name: 'home',
  data () {
    return {
          auth: auth.user.authenticated,
          }
  },
  components: {
      Room: room,
      Login: login
  },
  methods: {
    set(){
      sessionStorage.setItem('auth_token', 'item')
    }
  }

}
</script>

<style>

</style>
