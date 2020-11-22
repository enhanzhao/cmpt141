#Enhan Zhao 11097118

prairie_pirates = [
    ['Tractor Jack', 1000, True],
    ['Plowshare Pete', 950, False],
    ['Prairie Lily', 245, True],
    ['Red River Rosie', 350, True],
    ['Mad Athabasca McArthur', 842, False],
    ['Assiniboine Sally', 620, True],
    ['Thresher Tom', 150, True],
    ['Cranky Canola Carl', 499, False]
]


# part a)
best_plunderers = [x for x in prairie_pirates if x[1] > 400]   

# part b)
parrot_haters = [x for x in prairie_pirates if x[2] == False]  

# part c)
plunder_values = [(42 * x[1]) for x in prairie_pirates ]   

# part d)

names_and_plunder_values = [[x[0], x[1] * 42] for x in prairie_pirates if x[2] == True] 


    
print(best_plunderers)
print(parrot_haters)
print(plunder_values)
print(names_and_plunder_values)