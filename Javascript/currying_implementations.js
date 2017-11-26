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

let ezraDragon = dragon2('Ezra')
let tinyDragon2 = ezraDragon('tiny')
console.log('[LODASH]:', tinyDragon2('peas'))


// _.curry + filter().
let dragons = [
	{ name: 'fluffykis', element: 'lightning' },
	{ name: 'noomi', element: 'lightning' },
	{ name: 'karo', element: 'fire' },
	{ name: 'doomer', element: 'timewarp' }

]

let hasElement = _.curry((element, obj) => obj.element === element);

let lightningDragons = dragons.filter(hasElement('lightning'));
for (var x in lightningDragons) {
	console.log('[NO CURRY]:', lightningDragons[x])
}
