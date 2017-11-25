
def DNA_strand(dna):
# Giving a string composed of AGTC, return a string translating each character to it's complement (A<->T, G<->C).

  comp = ''
  for i in dna:
    if i == 'A':
      comp += 'T'
    if i == 'T':
      comp += 'A'
    if i == 'G':
      comp += 'C'
    if i == 'C':
      comp += 'G'
  return comp
  
# More succinctly:
ref = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
def DNA_strand(dna):
  return ''.join([ref[x] for x in dna])
