#Enhan Zhao 11097118 CMPT 141(01) L09

def spaceTime(distance):
  """
  Takes a distance and return time it takes to travel that distance
  distance is a positive int or float in meters
  returns time required to travel the distance
  """
  if distance <= 1: 
    return 1 
  else: 
    return 1 + spaceTime(distance/2)
  
print("Team Rocket's drive requires:")
print("-", spaceTime(37), "minutes to travel 37m to the nearest Poke-stop")
print("-", spaceTime(40075000), "minutes to travel 40075000m for a round trip around the earth")
print("-", spaceTime(1.49 * (10**11)), "minutes to travel 149000000000.0 meters from our earth to our sun")
print("-", spaceTime(4*(10**16)), "minutes to travel 4 e +16 meters from our sun to the nearest star")
print("-", spaceTime(8.8* (10**26)), "minutes to travel 8.8 e +26 meters across the observable universe")
print()
print("blah blah blah taem rckt blstin' oof agein...")
