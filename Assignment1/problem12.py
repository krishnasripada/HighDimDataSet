import numpy as np
import matplotlib.pyplot as plt
import math
import sys

allSamples = {}
requiredData = {}
percentileData = {}

for n in range(1, 401):
    samples = []
    while len(samples)<10000:
        sample = np.random.standard_normal(n)
        norm = np.linalg.norm(sample,2)
        samples.append(np.true_divide(sample,norm))
    data = np.asarray(samples)[:,0]
    
    if n in [4,25,100,225,400]:
        plt.title("Projection of the N points on the axis defined by x1 for n="+str(n))
        plt.xlabel("Samples")
        plt.ylabel("Frequency")
        plt.hist(data, bins=100)
        #plt.savefig("hist_"+str(n)+".png")
        plt.show()
        plt.close()
    
    x, y = np.mean(data), np.var(data)
    temp=[]
    temp.append(x)
    temp.append(y)
    requiredData.update({n:temp})
    percentileData.update({n: np.percentile(data, 99)})

means = []
variances = []
for key, values in requiredData.items():
    means.append(values[0])
    variances.append(values[1])
plt.title("Mean and Variance of the distribution of projections as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Attribute")
plt.plot(requiredData.keys(), means, 'r-', label="Mean")
plt.plot(requiredData.keys(), variances, 'b-', label="Variance")
plt.legend(loc='center right')
plt.show()
plt.close()

plt.title("Epsilon(n) as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Epsilon(n)")
plt.plot(percentileData.keys(), percentileData.values(), 'b-')
plt.show()
plt.close()




