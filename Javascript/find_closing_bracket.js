function solve(str,idx){
  // Given a string and an index containing an opening bracket, return the index of the closing bracket.
  // If the index provided is not an opening bracket, return -1.
 let lv = 0
 if (str[idx] != '(') return -1
 for (i=idx; i<str.length; i++) {
    str[i] == '(' ? lv ++ :
    str[i] == ')' ? lv -- : null
    if (lv == 0) {return i}
 } 
}
