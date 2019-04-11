<template>
  <div>

<button @click="oauth">
  Login from vk
</button>

  </div>
</template>

<script>
import auth from './utils/auth.js'

export default {
  name: 'login',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
      oauth(){
          var auth_url = auth.get_redirect()
        },
      }

}
</script>

<style>

</style>
