
const RoomTemplate = '<div class="card"> <button :data-id=id :data-action=msgs @click=open > open </button>' +
  '<div class="card-body">'+
     '<h5 class="card-title">{{ room_name }}</h5>'+
      '{{ msg_text }} {{ msg_date }}  {{ count_msgs }}'+
  '</div>'+
'</div>'



const MsgTemplate = '<div class="card">' +
  '<div class="card-body">'+
      '<p>{{ msg_text }}</p> <p>{{ date }}</p>  <p>{{ author }}</p>'+
  '</div>'+
'</div>'



const UserTemplate = '<div class="card">' +
  '<div class="card-body">'+
      '<p>{{ name }}</p> <p>{{ last_seen }}</p>   <button class="modal-default-button" @click="open_room" :data-id=id>Msg</button>'+
  '</div>'+
'</div>'



Vue.component('users', {
     template: UserTemplate,
     props: ['id', 'name', 'last_seen'],
     methods:{
        open_room(e){
             var id = e.target.getAttribute('data-id')
             var token = sessionStorage.getItem('auth_token')
             data = JSON.stringify({'method': 'POST', 'data': {'user_id': id}, 'url': '/api/room/', 'id': 'start-dialog', 'headers': {'Authorization': 'Token ' + token}})
             app.ws.send(data);
        },
     }
})

Vue.component('room', {
  template: RoomTemplate,
  props: ['id', 'room_name', 'msg_text', 'msg_date', 'count_msgs', 'msgs'],
  methods: {
        open(e){
                var msgs_url = e.target.getAttribute('data-action')
                app.msgs_url = msgs_url
                var token = sessionStorage.getItem('auth_token')
               data = JSON.stringify({'method': 'GET', 'url': msgs_url, 'id': 'detail-room', 'headers': {'Authorization': 'Token ' + token}})
               app.ws.send(data);

        },
  },

})

Vue.component('detail-room', {
    template: RoomTemplate,
    props: ['id', 'room_name', 'count_msgs', 'messages'],
    data() {
        return {msgs: []}
    },
     methods: {
            SendMessage() {
                console.log(this.text)
            },
        }
})




Vue.component('msg', {
  template: MsgTemplate,
  props: ['id', 'date', 'msg_text', 'name', 'author'],
})



var app = new Vue({
  el: '#app',
  data() {
    return {
        msgs_url: '',
        room_url: '',
        text: '',
        username: '',
        rooms: [],
        messages: [],
        users: [],
        name: null,
        password: null,
        showModal: false,
        auth: false,
        }
    },
//    computed: {
//       auth() {
////        this.ws = new WebSocket('ws://localhost:8000/');
////        var ws = this.ws
//        this.store = {}
//        this.id = 0
//        var token = sessionStorage.getItem('auth_token')
//
////        ws.onopen = function() {
////            var token = sessionStorage.getItem('auth_token')
////            if (token) {
////            data = JSON.stringify({'method': 'GET', 'url': '/api/room/', 'id': 'rooms', 'headers': {'Authorization': 'Token ' + token}})
////            app.ws.send(data);
////            }
////
////             data = JSON.stringify({'method': 'POST', 'url': '/api/event_subscribe/', 'id': '', 'headers': {'Authorization': 'Token ' + token}})
////            app.ws.send(data);
////        },
////        ws.onmessage = function (response) {
////                console.log(response)
////              var response = JSON.parse(response.data)
////              console.log(response, 'RESPONSE')
////              var status = Number(response['status_code'])
////              if ((status >= 200) && (status <= 300)) {
////                    app.dispatcher(response)
////              }
////              else {
////                    console.log(response)
////              }
////        }
////        ws.close = function() {
////            console.log('Close!')
////        }
//        return token
//        },
//    },
  created: function () {

     var token = sessionStorage.getItem('auth_token')

     if (token) {
     this.auth = true
    }

    this.ws = new WebSocket('ws://localhost:8000/');
    var ws = this.ws

   ws.onopen = function() {
        var token = sessionStorage.getItem('auth_token')
        if (token) {
        data = JSON.stringify({'method': 'GET', 'url': '/api/room/', 'id': 'rooms', 'headers': {'Authorization': 'Token ' + token}})
        app.ws.send(data);
        }

         data = JSON.stringify({'method': 'POST', 'url': '/api/event_subscribe/', 'id': '', 'headers': {'Authorization': 'Token ' + token}})
        app.ws.send(data);
    },
    ws.onmessage = function (response) {
            console.log(response)
          var response = JSON.parse(response.data)
          console.log(response, 'RESPONSE')
          var status = Number(response['status_code'])
          if ((status >= 200) && (status <= 300)) {
                app.dispatcher(response)
          }
          else {
                console.log(response)
          }
    }
    ws.close = function() {
        console.log('Close!')
    }






  },
    methods: {
        dispatcher(response){
            var func = response['id']
            console.log(func)
            console.log(response['data'], 'DISPatch')
            if (func) {
            temp[func](response['data'])
            }
        },

        close_modal: function() {
            this.showModal = false

        },

       open_modal: function() {
            this.showModal = true


        },
        SearchUsers: function(){
            var token = sessionStorage.getItem('auth_token')
            data = JSON.stringify({'method': 'GET', 'params': {'search': this.username}, 'url': '/auth/users/', 'id': 'list-users', 'headers': {'Authorization': 'Token ' + token}})
            this.ws.send(data);

        },

        login_func: function (data){
            console.log(data)
            sessionStorage.setItem('auth_token', data['auth_token'])
            this.token = data['auth_token']
            data = JSON.stringify({'method': 'GET', 'url': '/api/room/', 'id': 'rooms', 'headers': {'Authorization': 'Token ' + this.token}})
            this.ws.send(data);
            this.event_subscribe()
            this.auth = true
        },

        event_subscribe: function(){
            var token = sessionStorage.getItem('auth_token')
            data = JSON.stringify({'method': 'POST', 'url': '/api/event_subscribe/', 'id': '', 'headers': {'Authorization': 'Token ' + token}})
            this.ws.send(data);
        },

        make_rooms: function(data) {
            result = data['results']
            result.forEach(function push(item, index) {
            app.rooms.push({'room': {

           'id': item['url'],
           'name': item['name'],
           'msg_text': item['last_msg']['text'],
            'msg_date': item['last_msg']['date_created'],
             'count_msgs': item['count_msgs'],
             'msgs': item['messagfes'],
           },
           'type': 'room'})
          })

        },
        detail_room: function(data) {
            result = data['results']
           result.forEach(function push(item, index) {
            console.log(item, item['author']['username'])
            index = app.messages.push({'msg': {
                       'id': item['id'],
                        'name': item['name'],
                        'msg_text': item['text'],
                        'date': item['date_created'],
                        'author': item['author']['username']
                         },
                         'type': 'msg'})
                     })

             this.room_url = data['url']
             console.log(this.room_url)
            $('#room-textarea').show()


           },
        load_msgs: function(){
            var token = sessionStorage.getItem('auth_token')
            next = this.msgs['next']
            if (next) {
                data = JSON.stringify({'method': 'GET',  'url': next, 'id': 'detail-room', 'headers': {'Authorization': 'Token ' + token}})
                 this.ws.send(data);

            }


        },
        new_message: function(data){

            app.messages.push({'msg': {
                       'id': data['id'],
                        'name': data['name'],
                        'msg_text': data['text'],
                        'date': data['date_created'],
                        'author': data['author']['username']
                         },
                         'type': 'msg'})
        },

        list_users(data) {
            result = data['results']
           result.forEach(function push(item, index) {

            index = app.users.push({'users': {
                       'id': item['id'],
                        'name': item['username'],
                        'last_seen': item['text'],
                         },
                         'type': 'users'})
                     })

        },
        onLogin() {

           data = JSON.stringify({'method': 'POST', 'url': '/auth/token/login/', 'id': 'login_func', 'data': {'username': this.name, 'password': this.password}})
           this.ws.send(data);
        },
        SendMessage(e){
             var msgs_url = this.msgs_url
              var token = sessionStorage.getItem('auth_token')
             data = JSON.stringify({'method': 'POST', 'data': {'text': this.text}, 'url': msgs_url, 'id': 'new-message', 'headers': {'Authorization': 'Token ' + token}})
             this.ws.send(data);
        },
        start_dialog(data){
            console.log(data)
            this.showModal = false
            item = data

            app.rooms.push({'room': {
           'id': item['id'],
           'name': item['name'],
           'msg_text': item['last_msg']['text'],
            'msg_date': item['last_msg']['date_created'],
             'count_msgs': item['count_msgs'],
              'msgs': item['messages']
           },
           'type': 'room'})

           var token = sessionStorage.getItem('auth_token')
           data = JSON.stringify({'method': 'GET', 'url': item['messages'], 'id': 'detail-room', 'headers': {'Authorization': 'Token ' + token}})
            this.ws.send(data);



        }
     }
})



var temp = {'login_func': app.login_func,
            'rooms': app.make_rooms,
            'detail-room': app.detail_room,
             'new-message': app.new_message,
             'list-users': app.list_users,
             'start-dialog': app.start_dialog}


//
//    'id':1,
//    'status_code': 200,
//    'data': []
//
//}