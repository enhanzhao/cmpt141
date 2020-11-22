#Enhan Zhao 11097118 CMPT 141 (01) L09
import matplotlib.pyplot as plt
def population_growth(year1, n, r, K):
  """
  Calculatespopulation in year n based on initial population in year 1, growth rate r, and max population K
  p1 is an int, the initial population in year 1
  n is an int greater than 0, the year which we want to compute the populatoin
  r is a float between 0.0 and 1.0 representing the annual growth rate 
  K is hte max population that a ecosystem can support
  return the populatoin of year n
  """
  if n == 1:
    return year1
  else:

    P1 = population_growth(year1,n-1,r,K)
    r = r * (1 - P1 / K)
    P = P1*(1+r)
    return P

vals=[]
years=[]
for i in range(1,76):
  vals.append( population_growth(600,i,0.1,10000))
  years.append( i)

plt.plot(years,vals)
plt.xlim((0,70))
plt.ylim((0,10000))
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
plt.figure()

K=0
n=1
while K < 9900000000:
  K = population_growth(7000000000,n,0.011,10000000000)
  n+=1
print("The number of years it takes to exceed a pop. of 9.9 billion is ",n)


