function nbYear($p0, $percent, $aug, $p) {
  // Given a starting pop, pop growth %, and imcoming migrants per year, and target pop, return years to reach the target pop.
  echo "Start population: ", $p0, "\n";
  echo "Annual internal growth: ", $percent/100, "\n";
  echo "Newcomers per year: ", $aug, "\n";
  echo "Target population: ", $p, "\n";
  $year = 0; 

  while ($p0 < $p) {
    $p0 += ($p0 * $percent/100 + $aug);
    $year = $year + 1;
    echo "Current year: ", $year, "\n";
  }

  echo "Target pop reached: ", $p0, "\n";
  echo "Year: ", $year, "\n";
  return $year;
}
