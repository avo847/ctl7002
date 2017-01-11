import collections as coll
import numpy as np

import xlwt

class SumCounter:
  def __init__(self):
    self.data = {}
    
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
        
  def write_xls(self, filename):
    self.sort_data()
    book = xlwt.Workbook()
    sh = book.add_sheet("Sheet 1")
    
    sh.write(0,0, "sum")
    sh.write(0,1,"boxes of 6, 9, and 20")
    sh.write(0,2,"total nuggets")
    
    row_num=1
    for sum in self.data:
      if sum > 0:
        sh.write(row_num, 0, sum)
        for x in self.data[sum]:
          y = np.array(x)
          y[0] = 6*y[0]
          y[1] = 9*y[1]
          y[2] = 20*y[2]
          
          sh.write(row_num, 1, str(x))
          sh.write(row_num, 2, " + ".join(map(str,y))+ " = " + str(sum))
          row_num += 1
        
    book.save(filename)
    
        
# run code
my_sums = SumCounter()
my_sums.build()
my_sums.write_xls('output.xls')

    

