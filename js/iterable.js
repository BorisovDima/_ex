let array = ['a', 'b', 'c']

for(let i in array){
     console.log(array[i])
}
/////////////////////  OR ///////////////////
for(let i of array){
  console.log(i)
}
///////////////////////////////////////////
let obj_with_iter = {
  limit: 10,
  cur: 0,
  [Symbol.iterator]() {
    return this;
  },
  next(){
      if (this.cur < this.limit){
        return {
          done: false,
          value: this.cur++
        }
      }
      else{
        return {done: true}
      }
  }
}
for(let i of obj_with_iter){
  console.log(i)
}
