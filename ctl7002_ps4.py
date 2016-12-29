import numpy as np

  
def test_value(n):
  sum_less = n*(n-1)/2
  
  next= n+1
  sum_greater = 0

  while sum_greater < sum_less:
    sum_greater += next
    next += 1
  
  if sum_greater == sum_less:
    return next-1
  else:
    return 0

    
for n in np.arange(30, 40,1):
  total = test_value(n)
  if total != 0:
    print n, " works" 
    print "there are ", total, " houses on the block"