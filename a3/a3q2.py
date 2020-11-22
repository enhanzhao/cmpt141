#Enhan Zhao 11097118

import matplotlib.pyplot as plt

def supply (P):
	"""
	determines the number of units that can be manufactured according to P
	P is price
	returns the value of the price from supply

	"""
	supply_num = 500 + 90 * P
	return supply_num

def demand (P):
    """
	determines the number of units expected to sell according to P
	P is price
	returns the value of the price from supply

	"""
    demand_num = 10000 - 35 * P
    return demand_num
plt.figure()

for p in range(10, 161, 1):
    plt.plot(p, supply(p), "og")
    plt.plot(p, demand(p), "ob")
    if supply (p) == demand (p):
        eq_price = p
        plt.plot(p, demand(p), "ro")
print (eq_price)


plt.xlim ((0, 170))
plt.ylim ((0, 16000))
plt.xlabel ("Price of Special Edition (dollars)")
plt.ylabel ("Quantity Produced (units)")
plt.annotate ("Optimal Price", xy = (eq_price, supply(eq_price)))

plt.show()
plt.figure()
