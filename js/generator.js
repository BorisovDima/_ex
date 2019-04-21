function* gen(){
  yield 1
  yield 2
}
for(let i of gen()){
  console.log(i)
}
////////////////////////////////////



function* gen2(){
    yield* gen()
}
for(let i of gen2()){
  console.log(i)
}
//////////////////////////////////////////////
function* gen3(){
   let value = yield 'wait'
   console.log(value)

}
let generator = gen3()
console.log(generator.next())
generator.next('SEND')
