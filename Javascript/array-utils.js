// ALL: Returns true if the provided predicate function returns true for all elements in a collection, false otherwise
const all = (arr, fn = Boolean) => arr.every(fn)
console.log(all([1, 2, 3], x => x > 1))
console.log(all([1, 2, 3], x => x))

// ALLEQUAL: Check if all elements in an array are equal
const allEqual = arr => arr.every(val => val === arr[0])
console.log(allEqual([1, 2, 3]))
console.log(allEqual([1, 1, 1]))
console.log(allEqual([1, true]))
console.log(allEqual([false, null]))
console.log(allEqual([null, undefined]))

// ANY: Returns true if the provided predicate function returns true of at least one element in a collection, false otherwise.
// Use Array.prototype.some() to test if any elements in the collection return true based on fn. Omit the second argument, fn, to use Boolean as a default.
const any = (arr, fn = Boolean) => arr.some(fn)
console.log(any([1]))
console.log(any([0]))
console.log(any([0, 1]))
console.log(any([true]))
console.log(any([null]))
console.log(any([undefined, false, null, 0]))
console.log(any([2, 4, 6], x => x % 2))
console.log(any([2, 4, 5], x => x % 2))

// BIFURCATE: Splits values into two groups. If an element in filter is truthy, the corresponding element in the collection belongs to the first group; otherwise, it belongs in the second group.
// Use Array.prototype.reduce() and Array.prototype.push() to add elements to groups based on filter.
const bifurcate = (arr, filter) => arr.reduce((acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc), [[], []])
console.log(bifurcate(['beep', 'boop', 'foo', 'bar'], [true, true, false, true]))

// BIFURCATEBY: Splits values into two groups according to a predicate function, which specifies which group an element in the input collection belongs to. If the predicate function returns a truthy value, the collection element belongs to the first group; otherwise, it belongs to the second group.
const bifurcateBy = (arr, fn) => arr.reduce((acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc), [[], []])
console.log(bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b'))

// CHUNK: Chunks and array into smaller arrays of a specified size.
// Use Array.from to create a new Array, that fits the numbe fo chunks that will be produced. Use Array.prototype.slice() to map each element of the new array to a chunk the length of size. If the original array can't be split evenly, the final chunk will contain the remaining elements.
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) => arr.slice(i * size, i * size + size))
console.log(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
