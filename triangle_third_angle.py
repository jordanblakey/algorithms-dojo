function otherAngle($a, $b) {
  // Given two angles, return the third angle of a triangle.
  echo "Angles: ", $a, " ", $b, "\r\n";
  echo "Sum of Angles: ", $a + $b, "\r\n";
  echo "Third Angle: ", 180 - $a - $b;
  return 180 - $a - $b;
}
