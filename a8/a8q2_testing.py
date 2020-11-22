#Enhan Zhao 11097118 CMPT 141(01) L09


def ThreeSUM(in_list):
    """
    Determines whether or not there are three integers in the input list that sum to zero.
    :param : in_list a list of integers, any length
    :return: True if in_list contains three integers that sum to zero.
    """
    in_list.sort()
    
    if (len(in_list)) < 3:
        return False
        
    for first in range(0, len(in_list) - 2):
        a = in_list[first]
        second = first + 1
        third = len(in_list) - 1
        while second < third:
            b = in_list[second]
            c = in_list[third]
            if a + b + c == 0:
                return True
            if a + b + c > 0:
                third -= 1
            else:
                second += 1
        return False

test_ThreeSUM = [ {'inputs' : [0, 0, 0],
                'outputs': True,
                'reason' : "should return True as there are 3 zeros in sequence and their sum is zero"},
               {'inputs' : [0, 0, 1],
                'outputs': False,
                'reason' : "should return False, as there is no way for a sum of 0"},
               {'inputs' : [0, 0],
                'outputs': False,
                'reason' : "even though sequence sum is zero, it only contains 2 items"},
               {'inputs' : [0, 1],
                'outputs': False,
                'reason' : "sum is not zero, and sequence only contain 2 items"},
               {'inputs' : [0, 1, 1, 1, 0, 0, 1, 1, 1],
                'outputs': True,
                'reason' : "should return True if function iterates over the first item"},
               {'inputs' : [1, 1, 1, 1, 0, 0, 1, 1, 0],
                'outputs': True,
                'reason' : "should return True if function iterates over the last item"},
               {'inputs' : [],
                'outputs': False,
                'reason' : "should return False with empty sequence"},
               {'inputs' : [0, 10, 0, 10, 0],
                'outputs': True,
                'reason' : "test for when the intergers need for sum 0 is in the beginning, the middle and the end of the sequence"},
               {'inputs' : [-4, -2, -1, 1, 2, 3],
                'outputs': True,
                'reason' : "test for first second and third are at least one item away from each other"},
               {'inputs' : [-5, 0, 2, 3],
                'outputs': True,
                'reason' : "test for when first is at least one item away from second and third"},
               {'inputs' : [- 10, -11, 0, 1, 21, 20],
                'outputs': True,
                'reason' : "test for when third is at least one item away from first and second"},
             ]


for test in test_ThreeSUM:
    inputs = test['inputs']
    result = ThreeSUM(inputs) 
    if result != test['outputs']:
        print('Error: Returned', result, 'on inputs', inputs, '('+str(test['reason'])+')')
