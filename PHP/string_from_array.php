function smash(array $words): string {
  // Given an array of strings, return a single, space-separated, concatenated string. 
  print_r($words);
  $sent = join(" ", $words);
  return $sent;
}
