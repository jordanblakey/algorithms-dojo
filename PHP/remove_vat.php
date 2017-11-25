function excludingVatPrice($price){
  // Given numeric value for total price, return price with VAT of 15% removed.
  echo "Original price: $", $price, "\n";
  $price = round(($price / 1.15), 2);
  echo "After tax removal: $", $price, "\n";
  if (empty($price)) {return -1;}
  return $price;
}
