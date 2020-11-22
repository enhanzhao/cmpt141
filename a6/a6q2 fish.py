#Enhan Zhao 11097118

import numpy as np


######### PROVIDED FUNCTION, DO NOT MODIFY ############################################
def read_field(fname):
    '''
    Read data from a battlefield file.
    :param fname: The filename of the file containing battlefield data.
    :return: A 2D array of integers with penguin counts for each battlefield position.
    '''
    f = open(fname, 'r')
    data = []
    for row in f:
        line = [int(x) for x in row.rstrip().split(',')]
        data.append(line)
    return np.array(data)
########################################################################################


def find_target_location(battlefield, fish_weight):
  """
  determines the optimal target location 
  battlefield is a 2D interger array 
  fish_weight is an integer of weight of barrel fired/area covered
  returns optimal target location as a tuple (array offset)
  """
  max_enemy = 0
  max_cord_left = (0, 0)
  max_cord_center = (0, 0)
  side = 2 * fish_weight + 1
  if fish_weight >= ((len(battlefield))/2):
    return None 
  for row in range(len(battlefield) - side +1 ):
    for col in range(len(battlefield) - side +1 ):
      area = battlefield[row:row+side, col:col+side]
      if np.sum(area) > max_enemy:
        max_enemy = np.sum(area)
        max_cord_left = (row, col)
        max_cord_center = (max_cord_left[0] + int(side/2), max_cord_left[1] + int(side/2))
  return max_cord_center
     
field1 = read_field('field1.csv')
field2 = read_field('field2.csv')

print(find_target_location(field1, 1))
print(find_target_location(field1, 2))
print(find_target_location(field1, 3))
print(find_target_location(field2, 1))
print(find_target_location(field2, 2))
print(find_target_location(field2, 3))
print(find_target_location(field2, 4))
print(find_target_location(field2, 5))
