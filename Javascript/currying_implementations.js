// Currying in ES6
let dragon = 
  name =>
    size =>
      element =>
        name + ' is a ' +
        size + ' dragon that breathes ' +
        element + '!'

let fluffykinsDragon = dragon('fluffykins')
let tinyDragon = fluffykinsDragon('tiny')
console.log('[ES6]:', tinyDragon('lightning'))


// Currying using lodash
import _ from 'lodash'

let dragon2 = (name, size, element) =>
	name + ' is a ' +
	size + ' dragon that breathes ' +
	element + '!'

dragon2 = _.curry(dragon2)

let bobDragon = dragon2('Ezra')
let tinyDragon2 = bobDragon('tiny')
console.log('[LODASH]:', tinyDragon2('peas'))
