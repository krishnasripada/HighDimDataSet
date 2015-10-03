import numpy as np
import sys
import matplotlib.pyplot as plt
r = 1
accepted = []
rejected = {}
'''
for i in range(1, int(sys.argv[1])+1):
    for n in range(1, int(sys.argv[2])+1):
        samples = np.random.uniform(0,1,n)
        points = []
        for j in range(0, len(samples)):
            x = r*(1 - (2* samples[j]))
            points.append(x)
        points = np.asarray(points)
        if np.linalg.norm(points,2)<=r:
            accepted.append(points)
        #else:
            #rejected.update({n:len(points)})
    print "Finished ",i
accepted = accepted[:int(sys.argv[1])]
print np.asarray(accepted)
print len(accepted)
#print len(rejected)
'''
breaker = 0
for n in range(1, 401):
    counter = 0
    for i in range(1, 10001):
        samples = np.random.uniform(0,1,n)
        points = []
        for j in range(0, len(samples)):
            x = r*(1 - (2* samples[j]))
            points.append(x)
        if np.linalg.norm(points,2)<=r:
            accepted.append(points)
        else:
            counter+=1;
    rejected.update({n: counter})
    if counter==10000:
        print n
        breaker = n
        break

for n in range(breaker, 401):
    rejected.update({n: 10000})
print rejected

plt.title("No.of points rejected as a function of n")
plt.xlabel("Dimensions")
plt.ylabel("No.of points rejected")
plt.plot(rejected.keys(), rejected.values(),'b-')
plt.show()
plt.close()