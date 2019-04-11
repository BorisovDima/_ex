
export default {

  connect(){
    console.log('--------------', this)
   this.wsocket = new WebSocket('ws://localhost:8000/')
   this.wsocket.onmessage = this.recieve
   this.wsocket.store = this.store
 },
  recieve(response){
    var data = JSON.parse(response['data'])
    var pyload = data['data']
    if (data['id'] in this.store) {
        this.store[data['id']](pyload)
    }
  },

  store: {},
  counter: 0,

  send(data){
    var request = this.make_request(data)
    console.log(request)
    var count = 0
    function waitForSocketConnection(socket){
        count++
        if (count < 100000) {
        setTimeout(
            function () {
                if (socket.readyState === 1) {
                    console.log("Connection is made")
                    socket.send(request)
                }
                else {
                    console.log("wait for connection..." + count)
                    waitForSocketConnection(socket);
                }

            }, 10);
        }
      }
      waitForSocketConnection(this.wsocket)
  },
  get_id(){
    this.counter++
    return this.counter
  },
  make_request(data){
    var callback = data['callback']
    delete data['callback']
    var id = this.get_id()
    this.store[id] = callback
    data['id'] = id
    return JSON.stringify(data)
  }

}
