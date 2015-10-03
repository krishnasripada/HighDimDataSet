import numpy as np
import random
import sys
import math
import matplotlib.pyplot as plt
mu = 0
variance = 1
requiredData = {}

for n in range(1, 401):
    allSamples = []
    allSamplesNorm = []
    while len(allSamples) < 10000:
        samples = math.sqrt(variance) * np.random.randn(1, n)+mu
        allSamples.append(samples)
        allSamplesNorm.append(np.linalg.norm(samples,2))
    
    if n*n<400:
        if n*n in [4,25,100,225,400]:
            print n, np.asarray(allSamples)
    
    if n in [4,25,100,225,400]:
        plt.title("Histogram of the norm ||x|| of the points x for n = "+str(n))
        plt.xlabel("Samples")
        plt.ylabel("Frequency")
        plt.hist(allSamplesNorm, bins=100)
        #plt.savefig(str(n)+"_hist.png")
        plt.show()
        plt.close()

    x, y = np.mean(allSamplesNorm), np.var(allSamplesNorm)
    temp = []
    temp.append(x)
    temp.append(y)
    requiredData.update({n: temp})
    print "Done ",n

means = []
variances = []
for key, values in requiredData.items():
    means.append(values[0])
    variances.append(values[1])
plt.title("Mean and Variance of each distribution as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Attribute")
plt.plot(requiredData.keys(), means, 'r-', label="Mean")
plt.plot(requiredData.keys(), variances, 'b-', label="Variance")
plt.legend(loc='center right')
plt.show()
plt.close()