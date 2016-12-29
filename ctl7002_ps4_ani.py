import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  
compare_sums = np.zeros((10,2), dtype=np.int)

def sum_greater(n):
  sum_less = n*(n-1)/2
  
  next= n+1
  sum_greater = 0

  while sum_greater < sum_less:
    sum_greater += next
    next += 1
  return sum_greater

for n in np.arange(30, 40,1):
  #place sum of positive integers less than n
  compare_sums[n-30][0] = n*(n-1)/2
  
  # place sum oi integers greater than n
  compare_sums[n-30][1] = sum_greater(n)

print compare_sums

x=np.array([11,12,13,14,15,16,17,18,19,20])

df2 = pd.DataFrame(compare_sums, index=np.arange(30,40,1), columns=['sum less', 'sum greater'])

print df2

ax = df2.plot.bar();
ax.set_xlabel("House Number",fontsize=12)
ax.set_ylabel("Lower and upper sums",fontsize=12)

plt.show()