#Enhan Zhao 11097118 CMPT 141(01) L09

#what is the min number of wights required to break through defense with 95% success rate?

import random as random
import numpy as np
def read_field(scenario):
    '''
    Turn data from scenario file into a battlefield (array).
    :param scenario: The filename of the file containing battlefield data.
    :return: A 2D array of integers indicating static defense for each position
    '''
    f = open(scenario, 'r')
    data = []
    for row in f:
        line = [int(x) for x in row.rstrip().split(',')]
        data.append(line)
    f.close()
    return np.array(data[1:len(data)])
def is_success(scenario, start_number):
    """    calculates if the given number of wights can to break through human defense with 95% success rate
    :param scenario: a text file, first line contains GRIDSIZE, ARCHERSKILL, and SUCCESSNUMBRE; the rest is a N by N sized array
    :start_num: the starting number of wights
    :return: boolean based on if given number is successful
    """
    f = open(scenario, "r")
    data = []
    for row in f:
        line = [int(x) for x in row.rstrip().split(',')]
        data.append(line)
    f.close()
    n = data[0][0] #lengh of side
    skill = data[0][1] #archer skill
    k = data[0][2] #numder that must survive to be successful
#field, starting number assigned in each grid
    field = read_field(scenario)
    array_start = (np.zeros(len(field))) + start_number / (len(field))
#defense
    level = 0
    distance = len(field)
    while level < len(field):
#static defense
        array_start = array_start - field[level]
        level = level + 1
        distance = distance - 1
#active defense
        for i in range(len(array_start)):
            array_start[i] = array_start[i] - array_start[i]*((random.randint(0, max(0,skill-distance)))/100)
    remain = sum(array_start)
    if remain > k:
        return True
    else:
        return False
def find_percent(scenario, start):
    """
    find the % chance of success attack; runs is_success() 100 times
    :param scenario: txt file with information in first line and field as an array
    :param start: num of starting wight
    :return: percent chance of success attack in  attempts
    """
    count = 0
    count_true = 0
    while count < 100:
        if is_success(scenario, start) == True:
            count_true = count_true + 1
        count = count + 1
    return count_true/100
def find_start(scenario, start, end):
    """
    finds the number of starting wights needed for 95% success rate using binary search
    :param scenario: a txt file that contains info and array of battle field
    :param start: start int of a range
    :param end: end int of a range
    :return: the number of starting wights needed for 95% success rate
    """
    mid = (start + end) // 2
    x = find_percent(scenario, mid)
    if x >= 0.94 and x <= 0.96:
        return mid
    if x < 0.94:
        return find_start(scenario, mid+1, end)
    if x > 0.96:
        return find_start(scenario, start, mid-1)

#Max wights is 1 million
start = 0
end = 1000000
a = find_start("FistOfTheFirstMen.txt", start, end)
b = find_start("Hardhome.txt", start, end)
c = find_start("CastleBlack.txt", start, end)
d = find_start("TheWall.txt", start, end)

print("The minimum total number of wights for 95% success rate on FistOfTheFirstMen is", a)
if a > 1000000:
    print("The night king does not have enough wights.")

print("The minimum total number of wights for 95% success rate on Hardhome is", b)
if b > 1000000:
    print("The night king does not have enough wights.")

print("The minimum total number of wights for 95% success rate on CastleBlack is", c)
if c > 1000000:
    print("The night king does not have enough wights.")

print("The minimum total number of wights for 95% success rate on TheWall is", d)
if d > 1000000:
    print("The night king does not have enough wights.")

###########TESTCASE - is_success()#################################
#Input: "FistOfTheFirstMen.txt", 0
#Outut: False
#Reason: Tests a weak fortress with no starting wights

#Input: "FistOfTheFirstMen.txt", 100,000
#Outut: True
#Reason: Tests a weak fortress with 1/10 the max wights

#Input: "TheWall.txt, 0
#Outut: False
#Reason: Tests a very strong fortress with no starting wights

#Input: "TheWall.txt, 10000000000000000000000000000000
#Outut: True
#Reason: Tests a very strong fortress with a vry large amount wights


#test_suite_is_success = [  {'inputs' : ["FistOfTheFirstMen.txt", 0],
#                            'outputs': False,
#                            'reason' : "Tests a weak fortress with no starting wights"},
#                           {'inputs': ["FistOfTheFirstMen.txt", 100000],
#                            'outputs': True,
#                            'reason': "Tests a weak fortress with 1/10 the max wights"},
#                           {'inputs' : ["TheWall.txt", 0],
#                            'outputs': False,
#                            'reason' : "Tests a very strong fortress with no starting wights"},
#                           {'inputs' : ["TheWall.txt", 10000000000000000000000000000000],
#                            'outputs': True,
#                            'reason' : "Tests a very strong fortress with a vry large amount wights"}
#                           ]

#for test in test_suite_is_success:
#    inputs = test['inputs']
#    result = is_success(inputs[0],inputs[1])
#    if result != test['outputs']:
#        print('Error: Returned', result, 'on inputs',
#              inputs, '('+str(test['reason'])+')')

###########TESTCASE - find_percent()#################################
#Input: "FistOfTheFirstMen.txt", 0
#Outut: 0.0
#Reason: Tests a weak fortress with no starting wights

#Input: "FistOfTheFirstMen.txt", 1000000
#Outut: 1.0
#Reason: Tests a weak fortress with max starting wights

#Input: "TheWall.txt", 0
#Outut: 0.0
#Reason: Tests a very strong fortress with no starting wights

#Input: "TheWall.txt", 10000000000000000000000000000000000
#Outut: 1.0
#Reason: Tests a very strong fortress with a very large amount of wights

#test_suite_find_percent = [ {'inputs' : ["FistOfTheFirstMen.txt", 0],
#                'outputs': 0.0,
#                'reason' : "Tests a weak fortress with no starting wights"},
#                {'inputs' : ["FistOfTheFirstMen.txt", 1000000],
#                'outputs': 1.0,
#                'reason' : "Tests a weak fortress with max starting wights"},
#                {'inputs' : ["TheWall.txt", 0],
#                'outputs': 0.0,
#                'reason' : "Tests a very strong fortress with no starting wights"},
#                {'inputs' : ["TheWall.txt", 10000000000000000000000000000000000],
#                'outputs': 1.0,
#                'reason' : "Tests a very strong fortress with a very large amount of wights"},
#            ]

#for test in test_suite_find_percent:
#    inputs = test['inputs']
#    result = find_percent(inputs[0],inputs[1])
#    if result != test['outputs']:
#        print('Error: Returned', result, 'on inputs',
#              inputs, '('+str(test['reason'])+')')