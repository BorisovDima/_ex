class User{
  constructor(name){
    this.name = name
  }
  sayHi(){
      console.log(this.name)
  }
}
let one = new User('Jora')
one.sayHi()
console.log(one)
////////////////       OR         //////////////
function User1(name) {
  this.name = name;
}
User1.prototype.sayHi = function() {
  console.log(this.name);
};

let two = new User1('Jora')
two.sayHi()
///////////////////////////////////////////////////////////
class Model{

    constructor(name){
        this.first_name = (name)? name: ''
    }
    get name(){
      return this.first_name
    }
    set name(name){
      this.first_name  = name + ' set'
    }
    static create(name){
          return new User(name)
    }
}
let m = new Model()
m.name = 'Nmae'
console.log(m.name)

console.log(Model.create('Boris'))
////////////////////////////////////////////////////////////////////////

class Parent{
     constructor(name){
          this.name = name
     }
      method(){
        return this.name
      }
}

class Child extends Parent{
      method(){
          return super.method()
      }
}
let child = new Child('Boka')
console.log(child.method())
