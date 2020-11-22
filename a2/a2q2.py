#Enhan Zhao	11097118

#write function that performs subtas and return answer 

def fuel_efficiency (fuel_used, distance):

	"""
	Determines the duel efficiency of a car 
	fuel_used is the mount of fuel consumed
	distance is the total distance travelled
	returns fuel efficiency in L/100KM

	"""
	efficiency = fuel_used / distance * 100
	return efficiency

fuel = float(input ("How much fuel was used? (L): "))
travel_distance = float(input ("What is the distance traveled? (KM) :"))
fuel_efficiency (fuel, travel_distance)
print ("The fuel efficiency of a car that uses", fuel, "liters that travels", travel_distance, "KM is", str(fuel_efficiency(fuel, travel_distance))+".")