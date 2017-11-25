############################################################
# Refactored 
############################################################

def increment_string(strng):
  num = acc = lead_zeros = ''
  s = 0
  for c in strng[::-1]:
    if c.isdigit() and s == 0: num += c
    else:
      s = 1
      acc += c
  num = num[::-1]
  acc = acc[::-1]
  if num == '': return strng + '1'
  for i, c in enumerate(num):
    if c == '0' and i + 1 != len(num) and num[i + 1] != '9': lead_zeros += '0'
    else: break
  num = lead_zeros + str(int(num) + 1)
  return acc + num
  
# Even more succinctly:

def increment_string2(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


############################################################
# Original Solution
############################################################
def increment_string3(strng):
    # Given a string that ends in a number, increment that number, keeping leading zeros. If there is no number, append 1
    num = ''
    acc = ''
    lead_zeros = ''
    s = 0
    print(strng)
    for c in strng[::-1]:
        if c.isdigit() and s == 0: num += c
        else:
            s = 1
            acc += c
    num = num[::-1]
    acc = acc[::-1]
    print('string:', acc)
    print('number:', num)
    if num == '': return strng + '1'
    for i, c in enumerate(num):
        print('i', i, len(num))
        if c == '0': 
            if i+1 != len(num) and num[i+1] != '9': lead_zeros += '0'

        else: break
        print('lead_zeros:', lead_zeros)
    num = lead_zeros + str(int(num)+1)

    print(acc + num)
    return acc + num
