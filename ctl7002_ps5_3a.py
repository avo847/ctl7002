import collections as coll
import numpy as np

class SumCounter:
  def __init__(self):
    self.data = {}
    self.addends =[6,9,20]
    
  def add_sum(self, x, tuple):
    try:
      self.data[x].append(tuple)
    except KeyError:
      self.data[x] = coll.deque()
      self.data[x].append(tuple)
      
  def sort_data(self):
      self.data = coll.OrderedDict(sorted(self.data.items()))

  def data_exists(self, x , tuple):
    try:
      list = self.data[x]
    except KeyError:
      return 0;
    num = list.count(tuple)
    return num

  def build(self, max=50):
    xlim = max/6+1
    ylim = max/9+1
    zlim = max/20+1
    
    print xlim, ylim, zlim 
    for x in np.arange(0,xlim):
      for y in np.arange(0,ylim):
        for z in np.arange(0, zlim):
          pot_sum = 6*x + 9*y + 20*z
          if pot_sum <= max:
            self.add_sum(pot_sum, [x,y,z])
    
  def print_sums(self):
    self.sort_data()
    for sum in self.data:
      print sum, ": "
      for x in self.data[sum]:
        print x

        
# test code
my_sums = SumCounter()
my_sums.build()
print "ok"
my_sums.print_sums()

    

