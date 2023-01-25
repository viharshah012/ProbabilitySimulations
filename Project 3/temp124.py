import numpy as np

def Mnof(n):
    xvals = np.random.rayleigh(57, n)
    Mn = sum(xvals)/n
    return Mn

print(Mnof(30))
# sum1 = 0
# for i in range(10):
#     sum1 += Mnof(10)
# mean = sum1/10
# print(mean)