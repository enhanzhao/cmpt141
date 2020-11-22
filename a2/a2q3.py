#Enhan Zhao 	11097118

def trip_cost (flight_cost, room_cost_per_night, number_of_people, number_of_night):
	"""
	Calculates total cost of trip
	flight_cost is cost of flight per person in dollars
	room_cost_per_night is cost of a double room hotel per night in dollars
	number_of_pepole is the total amount of people
	number of night is the total number of nights 
	returns the total cost of the trip 
	"""
	number_of_rooms = number_of_people // 2 + number_of_people % 2
	room_cost_total = room_cost_per_night * number_of_night *number_of_rooms 
	flight_cost_total = flight_cost * number_of_people
	total_cost = flight_cost_total + room_cost_total 
	return total_cost

flight_price = float(input ("Enter cost of flight ($): "))
room_price_per_night = float(input ("Enter cost of a double room per night ($): "))
head_count = int(input ("Enter the number of people: "))
time = int(input ("Enter the number of nights: "))

print ("The total cost of the trip is $"+str(trip_cost(flight_price, room_price_per_night, head_count, time))+".")