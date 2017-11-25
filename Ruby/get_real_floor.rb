def get_real_floor(n)
  # Given an int representing a bldg floor, return the actual floor as counted from street level.
  if n < 0
    return n
  else if n < 13
    print n
    if n == 0
      return 0
    end
    return n - 1
  else
    return n - 2
  end
  end
end

# More succinctly
def get_real_floor2(n)
  n >= 1 ? (n > 13 ? n-2 : n-1) : n
end
