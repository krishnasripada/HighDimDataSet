import numpy as np
import matplotlib.pyplot as plt
import math
import sys

for n in range(1, 401):
    r = math.sqrt(n)
    samples = []
    distanceFromOrigin = []
    while len(samples)<10000:
        sample_normal = np.random.standard_normal(n)
        sample_uniform = np.random.uniform(0,1)
        sample_normal_norm = np.linalg.norm(sample_normal,2)
        samples.append(r * math.pow(sample_uniform,(1/float(n))) * np.true_divide(sample_normal,sample_normal_norm))

    distanceFromOrigin = [np.linalg.norm(sample,2) for sample in samples]

    if n in [4, 25, 100, 225, 400]:
        #print samples
        plt.title("Distance to the origin for all the points in the ball for n = 1,...,400")
        plt.xlabel("Distance")
        plt.ylabel("Frequency")
        plt.hist(distanceFromOrigin, bins = 100)
        plt.savefig("21_hist_"+str(n)+".png")
        plt.close()
    print "Done ",n

