def reverse_seq(n)
  # Given an integer n, return an array [1..n]
  foo ||= []
  while n > 0
    foo << n
    n -= 1
  end
  return foo
end

# More succinctly:
def reverse_seq(n)
  n.downto(1).to_a # Count down to 1 and push to an array
end
