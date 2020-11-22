#Enhan Zhao	11097118



def baseboard (width, length):
	"""
	Calculate total cost of baseboard
	width is the width of the room
	length is the length of the room
	returns the total cost of the baseboard based on room perimeter and cost of baseboard per foot
	"""
	cost_baseboard_ft = float(input ("What is the cost of baseboard per foot? :"))
	perimeter = 2 * width + 2 * length
	baseboard_total_cost = perimeter * cost_baseboard_ft
	return baseboard_total_cost

	

def carpet (width, length):
	"""
	Calculate total cost of carpet
	width is the width of the room
	length is the length of the room
	returns the total cost of the carpet based on the area of the room and cost of baseboard per square foot
	"""
	cost_carpet_sqft = float(input ("What is the cost of carpet per square foot? :"))
	area = width * length
	carpet_total_cost = area * cost_carpet_sqft
	return carpet_total_cost

def cost (baseboard, carpet):
	"""
	Calculate the total cost of renovating the room
	baseboard is the total cost of the baseboard
	carpet is the total cost of the carpet
	returns total cost including labour fee
	"""
	total_cost = 500 + baseboard + carpet
	return total_cost

l = float(input ("What is the length of the room (ft)? :"))
w = float(input ("What is the width of the room? :"))

print ("For a room of width", w, "and length", l, "the cost of the reno is $"+str(cost(baseboard(w, l), carpet(w, l))))