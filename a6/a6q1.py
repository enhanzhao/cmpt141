#Enhan Zhao 11097118

import numpy as np
import csv
import copy
#a
f = open('age_statistics.csv', 'r')
csvreader = csv.reader(f, delimiter=',')
data = []
for row in csvreader:
    row1 = [item.replace(',', '') for item in row]  
    data.append(row1)
f.close()
data1 = data[9:len(data)]
#b
data2 = copy.deepcopy(data1)
for i in data2:
  del i[0]
for i in data2:  
  for j in range(5):
    i[j] = int(i[j])
#c
row_age_dct = {}
for i in range(0,21):
  row_age_dct[i] = data1[i][0]
#d
data_array = np.array(data2)
#e
print(data_array.ndim)
print(data_array.size)
print(data_array.shape)
print(data_array.dtype)
#f
x = np.sum(data_array, (0))
print("The total population in year 2013 is", x[0])
print("The total population in year 2014 is", x[1])
print("The total population in year 2015 is", x[2])
print("The total population in year 2016 is", x[3])
print("The total population in year 2017 is", x[4])
#g
def percentage_change(array, n):
  """
  calculate the year over year % change of an age group at row index
  array is a 2D array containing the population data
  n is an int that refers to row index in the 2D array
  returns a 1D array length of 4 that contains % change for 2014 -2017
  """
  change = [1,2,3,4]
  change[0] = (array[n,1] - array[n,0])/array[n,0]*100
  change[1] = (array[n,2] - array[n,1])/array[n,1]*100
  change[2] = (array[n,3] - array[n,2])/array[n,2]*100
  change[3] = (array[n,4] - array[n,3])/array[n,3]*100
  change_per = np.array(change)
  return change_per
#h
print (percentage_change(data_array , 0))
print (percentage_change(data_array , 10))
print (percentage_change(data_array , 19))
print (percentage_change(data_array , 20))
#i
abs_change = []
average = []
for i in range(len(data_array)):
  abs_change.append(percentage_change(data_array, i))
for i in abs_change:
  average.append((abs(i[0])+abs(i[1])+abs(i[2])+abs(i[3]))/4)

print("The age group with the highest absolute year-over-year-percentage-change is", row_age_dct[average.index(max(average))]+".")
