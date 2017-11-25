################################################################
REFACTORED SOLUTION
################################################################

from itertools import product
def get_pins(obs):
  p = { '1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'], '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'], '8': ['5', '7', '8', '9', '0'], '9': ['6', '8', '9'], '0': ['0', '8'] }
  def perm(a, b):
    return sorted(set([''.join([str(y) for y in x]) for x in list(product(a, b))]))
  def acc(o):
    obs = list(o)
    acc = []
    for key in o:
      acc.append(p[str(key)])
    return acc
  def pol():
    prev = []
    res = []
    for acp in acc(obs):
      res = acp
      if prev != []:
        res = perm(prev, acp)
      prev = res[:]
    return res
  return pol()


################################################################
ORIGINAL SOLUTION
################################################################

# from itertools import permutations, repeat
from itertools import product

def get_pins2(observed):
    '''
    Given a sequence of observed presses on 9-digit keypad, return a list of possible PIN which allows for obsevation errors.
    Possible errors include any adjacent key for each press.
    '''
    
    # Possible values for each observed keypad press
    poss = {
        '1' : ['1','2','4'],
        '2' : ['1','2','3','5'],
        '3' : ['2','3','6'],
        '4' : ['1','4','5','7'],
        '5' : ['2','4','5','6','8'],
        '6' : ['3','5','6','9'],
        '7' : ['4','7','8'],
        '8' : ['5','7','8','9','0'],
        '9' : ['6','8','9'],
        '0' : ['0','8']
    }


    # Given two lists, return a list of all combinations between them
    def perm(a, b):
        # sub = list(list(zip(q, w)) for (q, w) in zip(repeat(a), permutations(b))) # Failed on different array lengths
        # sub = [list(zip(x,b)) for x in permutations(a,len(b))] # Failed
        sub = list(product(a, b))
        # print('1. All combos as list of lists of tuples', '\n', sub, '\n')
        
        # sub = [y for x in sub for y in x]
        # print('2. All combos as list of tuples', '\n', sub, '\n')
        
        sub = sorted([''.join([str(y) for y in x]) for x in sub])
        # print('3. All combos as a list of concatenated strings', '\n', sub, '\n')

        sub = sorted(set(sub))
        # print('4. Set of all combos as a sorted list of strings.', '\n', sub, '\n')
        return sub
        
    # Debug perm ()
    #     a = ['23', '25', '26', '29', '33', '35', '36', '39', '63', '65', '66', '69'] 
    #     b = ['6', '8', '9'] 
    #     print(perm(a, b))
    
    def accumulator(o):
        observed = list(o) # convert string to list
        acc = []
        for key in o:
            acc.append(poss[str(key)]) #append the list<str> of possible values for key press
        print('Accumulator:\n', acc) #print a list of lists representing the possible values for the sequence of presses
        return acc
    
    def poss_list():
        # Given a list of lists of possible values for each press in sequence, return a list of possible combinations.
        prev = []
        result = []
        for acc_poss in accumulator(observed): # loop through each poss in acc
            result = acc_poss
            # print('PREVIOUS LIST \n', prev, '\n LIST TO MERGE \n', acc_poss, '\n')
            if prev != []: # check if there is a poss list availble from the previous loop
                result = perm(prev, acc_poss)
                # print('All combos from current and prev list:\n', result) # print all combinations from the prev and curr list
            prev = result[:] # assign the current poss to prev
            # print('prev:', prev) # print the updated prev list
        # print("\n FINAL RESULT:\n", result)
        return result
        
    return poss_list()
