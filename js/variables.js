const a = 12
let vari = 'I global'

if (1) {
  let vari = 'i in {}'
  console.log(vari)
}
console.log(vari)
for(let a=0; a<5; a++){console.log(a)}

let ar = []
for(let c = 0; c<5; c++){
    ar.push(function(){console.log(c)})

}
ar.forEach(function(i){
  i()
})

let [one, two] = 'Hello Gu'.split(' ')
console.log(one, two);

let [one1, ...rest] = [1,2,3,4,5];
console.log(one1, rest)

let [one2='Anon', two1='Knniga'] = []

console.log(one2, two1)
