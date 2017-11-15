def solution(digits):
  # Give a string of digits, return the largest 5 digit sequence.
  cur = 1
  acc = []
  for digit in digits:
    acc.append(digits[cur:cur+5])
    cur += 1
    acc = filter(lambda x: len(x) == 5, acc)
  return int(sorted(acc)[-1])
  
# Or, more succinctly:
def solution2(dd):
  return max(int(dd[i:i+5]) for i in range(len(dd) - 4))
