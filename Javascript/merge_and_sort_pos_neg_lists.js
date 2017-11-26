function mergeArrays(arr1, arr2) {
  // Given 2 lists with positive and negative numbers, return a merged and sorted list.
  function sortNeg(a,b){
    return a - b;
  }
  arr1 = arr1.concat(arr2).sort(sortNeg);
  arr1 = Array.from(new Set(arr1));
  return arr1;
}

// More succinctly:
function mergeArrays(a, b) {
  return [...new Set(a.concat(b))].sort((a,b)=>a-b)
}
