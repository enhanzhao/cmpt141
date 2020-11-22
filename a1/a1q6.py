#Enhan Zhao 11097118

#set total value of grains plundered in dollars
total = float(input ("Enter total amount of grains plundered in dollars: "))
#set numer of crew 
crew_size = float(input ("How many crew does Jack have? :"))
#set tracktor Jack's 30% share worth
share_jack = total * 0.3
#set crew's 70% share worth
share_crew = total - share_jack
#set what each crew's share
share_per_crew = share_crew / crew_size
#set amount Jack donates
donation = share_jack * 0.15
print ("")
print ("Enter the total value of grains plundered in dollars: ", total)
print ("Enter the number of crew Jack has: ", crew_size)
print ("Jack's 30% share of the loot in dollars is: ", share_jack)
print ("Crew's 70% share of the loot in dollars is: ", share_crew) 
print ("How much each crew member takes home in dollars: ", share_per_crew)
print ("Jack donates:", donation, "to the food bank.")