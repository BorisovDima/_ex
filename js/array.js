let array = [1,2,3]
array.splice(0, 2, 'NEW', 'N') // [ 'NEW', 'N', 3 ]
////////////////////////////////////////
let new_a = array.map((l) => l + ' MAP' ) // [ 'NEW', 'N', 3 ] [ 'NEW MAP', 'N MAP', '3 MAP' ]

///////////////////////////////////////////

array.sort((l) => 3 * l) // [ 'NEW', 'N', 3 ]
//////////////////////////////////////////

array.forEach((item, index, array) => console.log(item, index, array))
////////////////////////////////////////////////////////////////////
console.log(array.join('-')) // NEW-N-3

////////////////////////////////////////////////////////////
console.log(array.push(1000))
console.log(array.pop())

console.log(array.unshift(2000))
console.log(array.shift())
