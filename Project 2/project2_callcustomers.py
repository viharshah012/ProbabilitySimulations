import math
import random
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import statistics
import json

# run simulation 100,000 times
values = []

for run in range(0, 100_000):
    W = 0
    # numbers of calls made
    calls_made = 0
    while calls_made < 4:
        W += 6
        rand = random.uniform(0,1)
        # 0 = busy/voicemail, 1 = rings but unavailable, 2 = available
        calltype = 0
        if 0 <= rand <= 0.2:
            calltype = 0
        elif 0.2 < rand <= 0.5:
            calltype = 1
        else:
            calltype = 2

        # I - exponential random distribution with lamda = 1/8
        X = np.random.exponential(scale=8, size=None)

        # Y - random variable with linear function (30,0) to (60,1/15)
        class my_pdf(st.rv_continuous):
            def _pdf(self,x):
                return (((1/15)/30)*x)-(1/15)
        my_cv = my_pdf(a=30, b=60, name='my_pdf')

        # if busy/voicemail, then wait 5 sec
        if calltype == 0:
            W += (5 + 1)
            calls_made += 1
            continue

        # if rings but unavailable
        if calltype == 1:
            W += (20 + 1)
            calls_made += 1
            continue

        # if available
        if calltype == 2 and X <= 20:
            W += (X + 1 + my_cv.rvs())
            calls_made = 4
        # if available but took too long to answer
        elif calltype == 2 and X > 20:
            W += (20 + 1)
            calls_made += 1
            continue

    if run % 1000 == 0:
        print(f"{int(run/1000)} / 100")
    values.append(W)

values.sort()
mean = statistics.mean(values)
median = values[50_000]
print("mean and then median")
print(mean)
print(median)

npvalues = np.array(values)
with open("data.json", "w") as jsonFile:
    jsonData = json.dumps(values)
    jsonFile.write(jsonData)


with open("data.json", "r") as jsonFile:
    times = json.load(jsonFile)
# # 168 - 37 = 131 values, 131*5 = 655
plt.hist(times, bins = 262, range= (37,168))
plt.xlabel('Time Spent to Contact Customer (seconds)')
plt.ylabel('Frequency/Occurance (100,000 attempts)')
plt.title('Time Spent to Contact on Frequency of Occurance')
plt.show()

# CDF estimate of W
i = 37
cdf_estimate = []
count = 0
while i <= 168:
    for k in range(0,len(times)):
        if i == 37:
            search_for = 37
            break
        elif i-0.05 <= times[k] <= i+0.05:
            search_for = times[k]
            break
    try:
        cdf_estimate.append((times.index(search_for)/100_000))
    except ValueError:
        cdf_estimate.append(0)
    i += 2.62
    count += 1
print (cdf_estimate)
xs = np.linspace(37,168,50)
plt.plot(xs,cdf_estimate)
plt.xlabel('Time Spent to Contact Customer (seconds)')
plt.ylabel('Cumulative Probability for Time Spent (100,000 attempts)')
plt.title('Time Spent to Contact on Cumulative Probability')
plt.show()

# graph empirical CDF
y = []
z = np.linspace(37,168,50)
for m in range(0,len(z)):
    y.append(1/(1+(math.exp(-0.08*(z[m]-72.3658)))))
plt.plot(z,y)
plt.xlabel('Time Spent to Contact Customer (seconds)')
plt.ylabel('Cumulative Probability for Time Spent (100,000 attempts)')
plt.title('Time Spent to Contact on Cumulative Probability')
plt.show()