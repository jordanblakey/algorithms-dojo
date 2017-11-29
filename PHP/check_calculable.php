function calculator($a, $b, $sign) {
  // Given two variables of any type and an operator as a string, 
  // if the operator can be used with those values, return the result.
  // Else, return 'unknown value.'
  echo 'Given arguments: ' . $a . ', ' . $b . ', ' . $sign . "\nReturn: ";
  if (!is_numeric($a) || !is_numeric($b) || is_string($a) || is_string($b)){return 'unknown value';}
  switch($sign){
    case "+":
      echo $a + $b . "\n\n";
      return $a + $b;
      break;
    case "-":
      echo $a - $b . "\n\n";
      return $a - $b;
      break;
    case "*":
      echo $a * $b . "\n\n";
      return $a * $b;
      break;
    case "/":
      echo $a / $b . "\n\n";
      return $a / $b;
      break;
    case "%":
      echo $a % $b . "\n\n";
      return $a % $b;
      break;
    default:
      return 'unknown value';
      break;
  }  
}
