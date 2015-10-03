import numpy as np
from scipy.stats import bernoulli
from scipy.linalg import eig
import random
import matplotlib.pyplot as plt
import itertools, math

def generateWignerMatrix(matrix_size, i):
    matrix = np.zeros((matrix_size, matrix_size)) #Form a matrix
    newSize = (matrix_size*(i+1))/2
    bern = bernoulli.rvs(0.5, size=newSize) #Get the random bernoulli variates
    for i in range(0, len(bern)):
        if bern[i]==0:
            bern[i]=-1

    upperIndex = np.triu_indices(matrix_size)
    for x,y in zip(upperIndex[0], upperIndex[1]):
        matrix[x][y] = random.choice(bern)
    

    lowerIndex = np.tril_indices_from(matrix, k=-1)
    for x,y in zip(lowerIndex[0], lowerIndex[1]):
        matrix[x][y] = random.choice(bern)

    return matrix

def gaussianOrthogonalEnsemble(matrix_size, i):
    matrix = np.zeros((matrix_size, matrix_size)) #Form a matrix
    newSize = (matrix_size* (i+1))/2
    upperValues = np.random.normal(0,1, newSize)
    diagonalValues = np.random.normal(0,2, matrix_size)
    
    upperIndex = np.triu_indices_from(matrix, k=1)
    for x,y in zip(upperIndex[0], upperIndex[1]):
        matrix[x][y] = random.choice(upperValues)
    
    diagIndex = np.diag_indices(matrix_size)
    for x,y in zip(diagIndex[0], diagIndex[1]):
        matrix[x][y] = random.choice(diagonalValues)
    
    lowerIndex = np.tril_indices_from(matrix, k=-1)
    for x,y in zip(lowerIndex[0], lowerIndex[1]):
        matrix[x][y] = random.choice(upperValues)

    return matrix

wignerGaussian = {}
bernoulliMatrices = {}


print "Wigner Matrix for Bernoulli"
for n in [10,50,100,500,1000]:
    eigValues = []
    for i in range(1,101):
        matrix_size = n
        matrix = generateWignerMatrix(matrix_size,i)
        eighenValues = eig(matrix)[0]
        eigValues.append(eighenValues)
    
    eigValues = list(itertools.chain.from_iterable(eigValues))
    normedeigValues = np.true_divide(eigValues,math.sqrt(n)).tolist()
    bernoulliMatrices.update({n:normedeigValues})

print len(bernoulliMatrices)

print "Gaussian Orthogonal Ensemble"
for n in [10,50,100,500,1000]:
    eigValues = []
    for i in range(1,101):
        matrix_size = n
        matrix = gaussianOrthogonalEnsemble(matrix_size,i)
        eighenValues = eig(matrix)[0]
        eigValues.append(eighenValues)
    
    eigValues = list(itertools.chain.from_iterable(eigValues))
    normedeigValues = np.true_divide(eigValues,math.sqrt(n)).tolist()
    wignerGaussian.update({n:normedeigValues})

print len(wignerGaussian)

for key, value in bernoulliMatrices.items():
    plt.title("Bernoulli - Real Part vs Imaginary part on the complex space for eigen values for n="+str(key))
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    xValues = []
    yValues = []
    for x in value:
        xValues.append(x.real)
        yValues.append(x.imag)

    plt.plot(xValues, yValues, 'bo')
    plt.show()
    plt.close()

for key, value in wignerGaussian.items():
    plt.title("Gaussian - Real Part vs Imaginary part on the complex space for eigen values for n="+str(key))
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    xValues = []
    yValues = []
    for x in value:
        xValues.append(x.real)
        yValues.append(x.imag)
    
    plt.plot(xValues, yValues, 'bo')
    plt.show()
    plt.close()
