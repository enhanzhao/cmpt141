#Enhan Zhao 11097118

# Question 1

def index_responses(responses):
    """
    Takes a list of multiple choice responses and returns a dictionary of question-response pairs.
    responses is a list of multiple choice responses
    returns a dictionary of question-response key-value pairs
    """
    question_response = {}
    for i in range(1, len(responses)+1):
            question_response["Q"+str(i)] = responses[i-1]
    return question_response

#print('Testing index_responses()')
#print(index_responses(['a', 'b', 'c']))
#print(index_responses(['a','a','c','b']))
#print(index_responses(['d','d','b','e','e','e','d','a']))

# Question 2

def index_student(list):
    """
    Takes a list of student responses and returns a record dictionary 
    list is a list containing "ID", "Name", and "Responses"
    returns a record with fields: "ID", "Name", and "Responses"
    """
    record = {}
    record["ID"] = list[0]
    record["Name"] = list[1]
    response_list = list[2:len(list)]
    record["Responses"] = index_responses(response_list)
    return record

#print('Testing index_student()')
#print(index_student(['345','xyzzy','a','a','c','b']))
#print(index_student(['10021795','Samden Cross', 'd','d','b','e','e','e','d','a']))

# Question 3

def index_class(list_of_list):
    """
    Takes a list of list and returns a database
    list_of_list is a list of list that contains student responses
    returns database where the key is ID and the value is a student record
    """
    database = {}
    for i in range(len(list_of_list)):
        database[list_of_list[i][0]] = index_student(list_of_list[i])
    return database

#print('Testing index_class()')
#print(index_class([['123','foo', 'a','b','c','a'],
#                   ['234','bar', 'a','b','c','b'],
#                   ['345','xyzzy','a','a','c','b']]))
#print(index_class([['10021795','Samden Cross', 'd','d','b','e','e','e','d','a'],
#                   ['11051158','Jenni Nuxulon','d','d','b','e','e','d','d','a']]))

# Question 4

def grade_student(right_answers, response):
    """
    counts correct responses made
    right_answers is a dictionary of the answer key
    response is a dictionary one student's answers
    return count
    """
    count = 0
    for i in right_answers:
        if right_answers[i] == response[i]:
            count = count + 1
    return count

#print('Testing grade_student')
#answers = index_responses(['a','b','c'])
#resp1 = index_responses(['a','b','b'])
#resp2 = index_responses(['a','b','c'])
#print('Correct responses for first example:', grade_student(answers,resp1))
#print('Correct responses for second example:', grade_student(answers,resp2))

# Question 5

def grade(right_answers, database):
    """
    grades each student's responses and adds a new key-value pair to the data base
    right_answers is the dictionary of correct answers
    database is the response dictionary that contains all student informations
    returns nothing
    """
    for k in database:
        database[k]["Score"] = grade_student(right_answers, database[k]["Responses"])
        
#print('Testing grade')
#answers = index_responses(['a','b','c','b'])
#response_db = index_class([['123','foo', 'a','b','c','a'],
#                           ['234','bar', 'a','b','c','b'],
#                           ['345','xyzzy','a','a','c','b']])
#print('Response DB before')
#print(response_db)
#grade(answers,response_db)
#print('Response DB after')
#print(response_db)

# Question 6 

def read_response_file(file):
    """
    removes white space and newline at the end of each line of a tabular file and split into a list of list
    file is a file of responses in tabular format
    returns a list where each item is a line in the file as a list
    """
    f= open(file, "r")
    response = []
    for line in f:
        response.append([x.rstrip() for x in line.split(",")])
    f.close
    return response 

#print('Testing read_response_file')
#data = read_response_file('cmpt181_midterm.txt')
#print(data[0:3])

# Question 7

def write_score_file(file_name, database):
    """
    writes information from a database into a file
    file_name is the name of a file to be written
    database is a dictionary with student information
    retuns nothing
    """
    f = open(file_name, "w")
    names = database.keys()
    for i in names:
        f.write(database[i]["ID"]+","+database[i]["Name"]+","+str(database[i]["Score"])+"\n")

    f.close()
    
#print('Testing write_score_file')
#answers = index_responses(['a','b','c','b'])
#response_db = index_class([['123','foo', 'a','b','c','a'],
#                          ['234','bar', 'a','b','c','b'],
#                           ['345','xyzzy','a','a','c','b']])
#grade(answers,response_db)
#write_score_file('score_file_example.txt', response_db)

# Question 8

f = open("cmpt181_midterm.txt", "r")
list = []
for line in f:
    list.append([n.rstrip() for n in line.split(",")])
key = index_responses(list[0][2:len(list[0])])
f.close()

list_of_list = read_response_file("cmpt181_midterm.txt") #list of list
db = index_class(list_of_list) #database
grade(key, db)
write_score_file("Score_File.txt", db)

#Question 9

results = []
f = open("Score_File.txt", "r")
for line in f:
    results.append([n.rstrip() for n in line.split(",")])
f.close()
scores = [x[2] for x in results]
del scores[0]
for i in range(len(scores)):
    scores[i] = int(scores[i])

def print_score_report(n, scores):
    """
    prints to screen test results
    n is the number of questions in the test
    scores is a list of all the students scores
    returns nothing
    """
    import statistics as s
    highmarks = len([x for x in scores if x/n > 0.8])
    lowmarks = len([x for x in scores if x/n < 0.4])
    print("*****Scores summary*****")
    print("Number of students:", len(scores))
    print("Number of questions:", n)
    print("\tMinimum score:", min(scores))
    print("\tAverage score:", s.mean(scores))
    print("\tMedian score:", s.median(scores))
    print("\tMaximum score:", max(scores))
    print("There were", highmarks, "students who recieved a grade above 80%.")
    print("There were", lowmarks, "students who recieved a grade below 40%.")

print_score_report(30, scores)
