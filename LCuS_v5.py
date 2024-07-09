# Testing out reccurence relations for h 

import numpy as np
import sys
import random

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0


def h(i, k, l, m, seq):
  if gamma(k, i-1, seq) == 0 or gamma(k, m-1, seq) == 0:
      return k
  max = 0
  for r in range(gamma(k, i-1, i)):
      for s in range(gamma(k, m-1, m)): 
          temp = a(r, k-1, l, s) 
          if temp > max:
            max = temp
  return max

def a(i, k, l, m, seq): 
    if seq[i-1] == seq[k-1] == seq[m-1]:
        return h(i, k, l, m, seq)
    return min(a(i, k-1, l, m), h(i, k, l, m))