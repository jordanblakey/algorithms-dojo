function likes(names) {
  // Given an array of names for 'likes', return a formatted string to display who gave the likes.
  others = names.length - 2
  console.log(names, others)

  if (names.length == 0) { return 'no one likes this'}
  if (names.length == 1) { return names[0] + ' likes this'}
  if (names.length == 2) { return names.join(' and ') + ' like this'}
  if (names.length == 3) { return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'}
  if (names.length > 3) { return names[0] + ', ' + names[1] + ' and ' + others + ' others like this'}
}
