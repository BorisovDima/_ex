let promise = new Promise((ok_c, err_c)=>{
      setTimeout(()=>ok_c('Response'), 1000)
})
promise.then(
  (res) => {
    console.log(res, 'ok')
    },
 (err)=>{
      console.log(err)
})

/////////////////////////////////////////////////////
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

let promise2 = new Promise((ok, err)=>{
        let xhr = new XMLHttpRequest()
        xhr.open('GET', 'http://localhost', true)
        xhr.onload = function() {
          console.log(this.status)
          ok(this.respone)
        }
        xhr.send()
})
promise2.then((res)=>{console.log(res)})
