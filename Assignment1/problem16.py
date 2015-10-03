import numpy as np
import matplotlib.pyplot as plt
import math
import sys

requiredData = {}
percentileData = {}
for n in range(1, 401):
    samples= []
    r = math.sqrt(n)
    while len(samples)<10000:
        sample_normal = np.random.standard_normal(n)
        sample_uniform = np.random.uniform(0,1)
        sample_normal_norm = np.linalg.norm(sample_normal,2)
        samples.append(r * math.pow(sample_uniform,(1/float(n))) * np.true_divide(sample_normal,sample_normal_norm))

    data = np.asarray(samples)[:,0]

    if n in [4,25,100,225,400]:
        plt.title("Projection of the N points on the axis defined by x1 for n="+str(n))
        plt.xlabel("Samples")
        plt.ylabel("Frequency")
        plt.hist(data, bins=100)
        plt.savefig("17_hist_"+str(n)+".png")
        plt.close()

    x, y = np.mean(data), np.var(data)
    temp = []
    temp.append(x)
    temp.append(y)
    requiredData.update({n: temp})
    counter = 0
    for element in data:
        if element>=-0.5 and element<=0.5:
            counter+=1
    percentileData.update({n: counter/float(10000)})
    print "Done ",n


means = []
variances = []
for key, value in requiredData.items():
    means.append(value[0])
    variances.append(value[1])

plt.title("Mean and Variance of the distribution of projections as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Attribute")
plt.plot(requiredData.keys(), means, 'r-', label="Mean")
plt.plot(requiredData.keys(), variances, 'b-', label="Variance")
plt.legend(loc='center right')
plt.show()
plt.close()

plt.title("w(n) as a function of n")
plt.xlabel("Dimension")
plt.ylabel("w(n)")
plt.plot(percentileData.keys(), percentileData.values(), 'b-')
plt.show()
plt.close()