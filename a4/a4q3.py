#Enhan Zhao 11097118

quests = [
    ["Destroy the Rats in the Farmer's Basement", "Westhaven Farms", [1, 5], [1.0, 0.2]],
    ["Infiltrate the Bandit's Lair", "The Badlands", [2, 4], [40.0, 1]],
    ["Defeat Goliad", "Candy Kingdom", [20, 25], [10.0, 1.5]],
    ["Locate the Lich's Lair", "Costal Wasteland", [35, 40], [100.0, 10.0]],
    ["Atone for Shoko's Sins", "Finn's Treehouse", [15, 17], [0.0, 0.0]],
    ["Make an Amazing Sandwich", "Finn's Treehouse", [7, 11], [0.0, 0.0]],
    ["Find the Ice King's Wizard Eye", "Ice Kingdom", [9, 15], [25.0, 2.0]],
    ["Get some pickles from Prismo", "Prismo's Home", [27, 31], [42000000.0, 0.1]],
    ["Rescue Wildberry Princess from the Ice King", "Ice Kingdom", [3, 11], [25.0, 2.0]],
    ["Win Wizard Battle", "Wizard Battle Arena", [13, 18], [90.0, 7.0]],
    ["Eat Marceline's Fries", "Marceline's House", [3, 6], [16.0, 2.5]],
    ["Rescue Marceline from the Nightosphere", "The Nightosphere", [21, 27], [200.0, 1.5]],
    ["Discover Peppermint Butler's Secrets", "Candy Kingdom", [35, 40], [10.0, 1.5]],
    ["Defeat the Ice King's Penguin Army", "Candy Kingdom", [27, 29], [10.0, 1.5]],
    ["Discover the Ice King's Secret Past", "The Past", [10, 35], [0.5, 21.0]],
    ["Watch what Beemo Does When He Is Alone", "Finn's Treehouse", [1, 50], [0.0, 0.0]]
]


def create_quest(name, location, minlvl, maxlvl, distance, time):
	list = [name, location, [minlvl, maxlvl], [distance, time]]
	return list

quest_1 = create_quest("Kill the rebels", "continentx", 5, 10, 20.0, 16.0 )

quest_2 = create_quest("Infiltrate their base", "continentx", 10, 15, 33.3, 15.9)

quest_3 = create_quest("Confront the rebel leader", "continentx hideout", 25, 40, 45.0, 50.0)

quests.extend([quest_1])
quests.extend([quest_2])
quests.extend([quest_3])

#
def travel_time(query_quests, current_quests):
  t = [[x[3][1], x[1]] for x in current_quests if x[0] == query_quests]
  if t == []:
    print("There is no current quest named", query_quests)
  else: 
    print("It will take", t[0][0], "hours to journey to", t[0][1])

travel_time("Get some pickles from Prismo", quests)

travel_time("the quest that doesnt exist", quests)

def print_nearby_quests(max_distance, max_level, current_quests):
  #distance x[3[][0]  maxlevel x[2][1]     name x[0]
  t = [[x[0], x[1], x[3][1]] for x in current_quests if x[2][1] >= max_level and x[3][0] <= max_distance]
  for x in t:
    print(x[0], "at", x[1], "is nearby. You can get there in", x[2], "hours.") 

print_nearby_quests(20, 20, quests)