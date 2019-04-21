let map = new Map()
map.set(true, 1)
map.set('key', 'value')
let obj = {'obj_key': 'value'}
map.set(obj, 2)
console.log(map.get(obj))
map.keys() // { true, 'key', { obj_key: 'value' } }
map.values() // { 1, 'value', 2 }
map.delete('key')
map.clear() // {}


//////////////////////////////////////////////
let set = new Set()

set.add(1)
set.add(1)
set.add(2)
set.add(2)
set.add(3)

console.log(set) // { 1, 2, 3 }
