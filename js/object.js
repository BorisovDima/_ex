let attr = 12
let attr2 = 'zoo'
let obj = {
  attr,
  attr2
}
console.log(obj)

/////////////////////////////////////////////////////

let user1 = {name: 'Vasa', admin: true}
let user2 = {name:'Kola'}
let user3 = {}
Object.assign(user3, user1, user2);

console.log(user3)
let clone = Object.assign({}, user3)
console.log(clone)

//////////////////////////////////////////////////////////

let obj2 = {
  attr: 'MAGA',
  method(){
    console.log()
  },
  get name(){
    return this.attr
  },
  set name(arg){
    this.attr = arg
  }
}
console.log(obj2.name)
obj2.name = 'Hela'
console.log(obj2.name)
///////////////////////////////////////////
let parent = {
  attr: 'I parent',
  func(){
    console.log('parent method')
    return 'res'
  }
}
let child = {
  __proto__: parent,
  func(){
    let res = super.func()
    return res
  }
}

console.log(child.attr)
console.log(child.func())
