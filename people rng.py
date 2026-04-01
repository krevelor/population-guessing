#################################################################
#
# Quick program to investigate a question of derangements posed by my sister
# In her scenario, each person has to pick a number between 1
# and the number of people, inclusive. Anyone who picks the same number
# as another person loses.
# Our original discussion was about the pyschological aspect -
# what number would you pick? - but we became curious about
# the limiting behavior. If everyone picks randomly, how many people lose
# the game?
#
# Eden Carrier, 2025
#
 


import random
import matplotlib.pyplot as plt

# due to technical limitations I couldn't run this naive approach
# with the full ~8 billion population. however runs with increasing counts
# seem to converge to somewhere around a quarter of people losing
#eb = 8000000000
eb = 800000

# approach is simple - assign each person a number at random and put them in a list
buckets = [0] * eb

for i in range(eb):
    buckets[random.randint(0,eb-1)] += 1

# also investigating dynamics, so checking what most common response is
maxc = 0
for i in range(eb):
    if buckets[i] > maxc:
        maxc = buckets[i]

counts = [0] * (maxc + 1)

losers = 0
for i in range(eb):
    counts[buckets[i]] += 1
    if buckets[i] > 2:
        losers += buckets[i]


print(losers)
print(losers/eb)

# graphing how common each count is across the set of possible responses
x = []
for i in range(maxc + 1):
    x.append(i)


plt.plot( x, counts )
plt.show()
