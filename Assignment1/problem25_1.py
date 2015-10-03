import numpy as np
from scipy.stats import bernoulli
from scipy.linalg import eigh
import random
import matplotlib.pyplot as plt
import itertools
import math

def generateWignerMatrix(matrix_size):
    matrix = np.zeros((matrix_size, matrix_size)) #Form a symmetric matrix
    newSize = (matrix_size*(matrix_size+1))/2
    bern = bernoulli.rvs(0.5, size=newSize) #Get the random bernoulli variates
    for i in range(0, len(bern)):
        if bern[i]==0:
            bern[i]=-1

    i = 0
    upperIndex = np.triu_indices(matrix_size)
    for x,y in zip(upperIndex[0], upperIndex[1]):
        matrix[x][y] = bern[i]
        i+=1

    upperIndex = np.triu_indices_from(matrix, k=1)
    lowerIndex = np.tril_indices_from(matrix, k=-1)
    matrix[lowerIndex] = matrix[upperIndex] #To make it symmetric

    return matrix

def gaussianOrthogonalEnsemble(matrix_size):
    matrix = np.zeros((matrix_size, matrix_size)) #Form a symmetric matrix
    newSize = (matrix_size* (matrix_size-1))/2
    upperValues = np.random.normal(0,1, newSize)
    diagonalValues = np.random.normal(0,2, matrix_size)
    
    i=0
    upperIndex = np.triu_indices_from(matrix, k=1)
    for x,y in zip(upperIndex[0], upperIndex[1]):
        matrix[x][y] = upperValues[i]
        i+=1
    
    i=0
    diagIndex = np.diag_indices(matrix_size)
    for x,y in zip(diagIndex[0], diagIndex[1]):
        matrix[x][y] = diagonalValues[i]
        i+=1
    
    upperIndex = np.triu_indices_from(matrix, k=1)
    lowerIndex = np.tril_indices_from(matrix, k=-1)
    matrix[lowerIndex] = matrix[upperIndex] #To make it symmetric
    return matrix

print "Wigner Matrix for Bernoulli"
wignerGaussian = {}
bernoulliMatrices = {}
for n in [10,50,100,500,1000]:
    eigValues = []
    for i in range(1,101):
        matrix_size = n
        matrix = generateWignerMatrix(matrix_size)
        eighenValues = eigh(matrix, eigvals_only=True)
        eigValues.append(eighenValues)
    
    eigValues = list(itertools.chain.from_iterable(eigValues))
    bernoulliMatrices.update({n:eigValues})

print len(bernoulliMatrices)

print "Gaussian Orthogonal Ensemble"
for n in [10,50,100,500,1000]:
    eigValues = []
    for i in range(1,101):
        matrix_size = n
        matrix = gaussianOrthogonalEnsemble(matrix_size)
        eighenValues = eigh(matrix, eigvals_only=True)
        eigValues.append(eighenValues)
    
    eigValues = list(itertools.chain.from_iterable(eigValues))
    wignerGaussian.update({n:eigValues})

print len(wignerGaussian)

for key, value in bernoulliMatrices.items():
    plt.title("Bernoulli ESD for n="+str(key))
    plt.xlabel("Eigen Values")
    plt.ylabel("Frequency")
    plt.hist(value, bins=100, normed=True)
    plt.show()
    plt.close()

for key, value in wignerGaussian.items():
    plt.title("Gaussian ESD for n="+str(key))
    plt.xlabel("Eigen Values")
    plt.ylabel("Frequency")
    plt.hist(value, bins=100, normed=True)
    plt.show()
    plt.close()

for n in [10,50,100,500,1000]:
    semiCircleDist = {}
    for i in np.arange(-3, 3, 0.01):
        if abs(i)<=2:
            semiCircleDist.update({i: (1/float(2*math.pi)) * math.sqrt(4 - math.pow(abs(i),2))})
        else:
            semiCircleDist.update({i: 0})

    print len(semiCircleDist.keys())
    print len(semiCircleDist.values())
    plt.title("Semi-Circle Distribution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(semiCircleDist.keys(), semiCircleDist.values(), 'bo')
    plt.show()
    plt.close()





