#Enhan Zhao 11097118 CMPT 141(01) L09

def between(num1, num2, num3):
    """
    Takes 3 int and returns True if num 1 is between num2 and num3, not inclusive
    num1, num2, and num3 are intergers
    returns boolean value if num1 is larger than num2 and smaller than num3
    """
    if num1 > min(num2, num3) and num1 < max(num2, num3):
        return True
    else:
        return False

def majority3(num_list):
    """
    Takes a number list and returns True if more than half of the intergers are divisible by 3
    num_list is a sequence containing any number of ints
    returns boolean if more than half of the num_list is divisible by 3
    """
    div_3 = 0
    for i in num_list:
        if i % 3  == 0:
            div_3 += 1
    if div_3 > (len(num_list))/2:
        return True
    else:
        return False

test_between = [ {'inputs' : [50, 1, 100],
                'outputs': True,
                'reason' : "num1 is in between num2(low end) and num3(high end)"},
               {'inputs' : [50, 100, 1],
                'outputs': True,
                'reason' : "num1 is in between num2(high end) and num3 (low end)"},
               {'inputs' : [100, 1, 50],
                'outputs': False,
                'reason' : "num1 is greater than num2 and num3 thus not in between num2 and num3"},
               {'inputs' : [0, 0, 0],
                'outputs': False,
                'reason' : "all 3 numbers are zeros, thus num1 is not in between num2 and num3"},
               {'inputs' : [-50, -1, -100],
                'outputs': True,
                'reason' : "num1 is negative and inbetween num2 and num3, which are also negative intergers"},
               {'inputs' : [0, -1, 1],
                'outputs': True,
                'reason' : "num1 is in between num2 and num3, when one is negative and one is positive"}
             ]

test_majority3 = [ {'inputs' : [],
                'outputs': False,
                'reason' : "empty sequence, test the for loop in function"},
               {'inputs' : [1, 1, 0, 3, -3],
                'outputs': True,
                'reason' : "zeros, positive and negative numbers divisible by 3 are more than 50% of sequence. If one does not work then ouput will be False"},
               {'inputs' : [111111111111111111111111111111, 111111111111111111111, 111111111111111, 111111111111, 111111, 1, 1, 1],
                'outputs': True,
                'reason' : "tests 5 large positive numbers divisible by 3, should return True"},
               {'inputs' : [-111111111111111111111111111111, -111111111111111111111, -111111111111111, -111111111111, -111111, -1, -1, -1],
                'outputs': True,
                'reason' : "tests 5 small negative numbers divisible by 3, should return True"},
               {'inputs' : [2, 4, 5, 3, 3, 3],
                'outputs': False,
                'reason' : "exactly half the items in sequence are divisible by 3, test second if statement"},
               {'inputs' : [3],
                'outputs': True,
                'reason' : "only 1 item in sequence that is divisible by 3"}
             ]
for test in test_between:
    inputs = test['inputs']
    result = between(inputs[0], inputs[1], inputs[2]) 
    if result != test['outputs']:
        print('Error: Returned', result, 'on inputs', inputs, '('+str(test['reason'])+')')


for test in test_majority3:
    inputs = test['inputs']
    result = majority3(inputs)
    if result != test['outputs']:
        print('Error: Returned', result, 'on inputs', inputs, '('+str(test['reason'])+')')








