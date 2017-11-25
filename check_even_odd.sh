x="$1"
# Given an integer as stdin, return whether it is even or odd.
if [ $((x % 2)) -eq 0 ]
  then
    echo "Even"
  else
    echo "Odd"
  fi
