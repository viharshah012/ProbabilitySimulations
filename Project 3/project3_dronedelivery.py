import math
import numpy as np
from scipy.stats import norm
import scipy.stats as stats
import matplotlib.pyplot as plt


#sample mean of n values
def Mnof(n):
    xvals = np.random.rayleigh(57, n)
    Mn = sum(xvals)/n
    return Mn

#generate 250*7 values of 250 Mn with value n
nlist = [10,30,50,100,250,500,1000]
finallist = []
for i in nlist:
    for j in range(250):
        finallist.append(Mnof(i))

# scatterplot of finallist
xaxis = []
for i in nlist:
    for j in range(250):
        xaxis.append(i)

mean = 57*((math.pi/2)**(0.5))
plt.scatter(xaxis,finallist, 0.75)
plt.plot([0,1250], [mean, mean], color = "red", label = "Actual Mean")
plt.show()

# Central Limit Theorem

# 100k values of Mn with value n
nlist2 = [2,6,10]
listof2 = []
listof6 = []
listof10 = []

for i in range(100000):
    listof2.append(Mnof(2))

for i in range(100000):
    listof6.append(Mnof(6))

for i in range(100000):
    listof10.append(Mnof(10))

plt.hist(listof2,400)
plt.show()
plt.hist(listof6,400)
plt.show()
plt.hist(listof10,400)
plt.show()

# standardized sample mean
nlist3 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]


def standardizedSample(n):
    simulvals = []
    Mnvals = []
    # var_x = (4-math.pi)/(2*((1/57)**2))
    for i in range(100_000):
        simulvals.append(Mnof(n))
    mu_Mn = sum(simulvals)/100_000
    sumforstd = 0
    for j in range(n):
        sumforstd += ((simulvals[j]-mu_Mn)**2)
    stdev_Mn = math.sqrt(1/(n-1)*(sumforstd))
    for k in range(100_000):
        Mnvals.append((simulvals[k]-mu_Mn)/stdev_Mn)
    return Mnvals
plt.hist(standardizedSample(30),400)
plt.show()

# Use your {Zn(k)} values to estimate seven representative CDF probabilities: Z < -1.4, -1, -0.5, 0, 0.5, 1, 1.4
def findProb(k,n):
    cdf = sorted(standardizedSample(n))
    for m in range(100_000):
        if k-.0005 <= cdf[m] <= k+.0005:
            end_at = m
            break
        elif k-.005 <= cdf[m] <= k+.005:
            end_at = m
            break
        elif k-.05 <= cdf[m] <= k+.05:
            end_at = m
            break
    p = end_at/100_000
    return p
    # print(cdf)
    # print(p)
    # print(end_at)
    # print(cdf[end_at])

# Compare these seven CDF values to the corresponding values from a true standard normal CDF by computing the absolute value of the difference at these seven zvalues
# And take MADn which is the greatest of the seven differences
def maxofslice(items, start, end):
    return max(items[start:end])
def findMADs():
    listofns = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    listofks = [-1.4, -1, -0.5, 0, 0.5, 1, 1.4]
    listofprobs = []
    listofnormp = []
    listofabsdifs = []
    listofMADS = []
    for i in listofns:
        for j in listofks:
            listofprobs.append(findProb(j,i))
            listofnormp.append(norm.cdf(j))
    for k in range(7*15):
        listofabsdifs.append(abs(listofprobs[k] - listofnormp[k]))
    for l in range(0,15):
        listofMADS.append(maxofslice(listofabsdifs,7*l,(7*l)+6))
    print(listofnormp)
    print(listofprobs)
    print(listofabsdifs)
    print(listofMADS)

# findMADs()

MADs = [0.30835753872598687, 0.23225474606854288, .21716999999999997, 0.20653999999999997, 0.21933999999999998, 0.20032, 0.22746, 0.19316, 0.18464246127401307, 0.18313000000000001, 0.1817824612740131, 0.181482461274013130, 0.1812224612740131, 0.18043246127401314, 0.17845246127401315]
xax = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
plt.xlabel=("sample sizes")
plt.ylabel=("MAD")
plt.plot(xax, MADs)
plt.show()

# create a graph to show empirical CDF as seven dots for 2, 6, 10
listofk = [-1.4, -1, -0.5, 0, 0.5, 1, 1.4]
pointsfor2 = [findProb(-1.4,2), findProb(-1,2), findProb(-0.5,2), findProb(0,2), findProb(0.5,2), findProb(1,2), findProb(1.4,2)]
pointsfor6 = [findProb(-1.4,6), findProb(-1,6), findProb(-0.5,6), findProb(0,6), findProb(0.5,6), findProb(1,6), findProb(1.4,6)]
pointsfor10 = [findProb(-1.4,10), findProb(-1,10), findProb(-0.5,10), findProb(0,10), findProb(0.5,10), findProb(1,10), findProb(1.4,10)]

plt.scatter(listofk,pointsfor2,c="red")
plt.scatter(listofk,pointsfor6,c="blue")
plt.scatter(listofk,pointsfor10,c="green")
plt.plot(np.linspace(-3,3,100), stats.norm.cdf(np.linspace(-3,3,100),0,1))
plt.show()

