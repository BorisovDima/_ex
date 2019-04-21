let func = (x, y) => y + x;
let func1 = () => 2 * 2;

console.log(func(12, 12))
console.log(func1())
/////////////////////////////////////////////////////

let biGfunc = (arg, ...args) => {
    let answer = {}
    args.forEach((i)=>{
        answer[i] = i + arg
    })
    return answer
}
console.log(biGfunc(6, 1,2,3,4,5, ...[6,7,8]))
/////////////////////////////////////////////////////

let c = {
  f: function(){
    console.log(this, 'this');
    (() => {console.log(this)})(); // this нет, беру из замыкания
  }
}
c['f']()
/////////////////////////////////////////////////////////

let f = (a='test') => a
console.log(f())
//////////////////////////////////////////////////////////

let opt = {one: 1,
          two: 2}
let f2 = ({one, two}) => [one, two];
let [o, t] = f2(opt)
console.log(o, t)
