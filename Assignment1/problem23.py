import numpy as np
from scipy.stats import bernoulli
from scipy.linalg import eigh
import random
import matplotlib.pyplot as plt
import itertools

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
        data = []
        data.append(np.amin(eighenValues))
        data.append(np.amax(eighenValues))
        eigValues.append(data)

    bernoulliMatrices.update({n:eigValues})

print len(bernoulliMatrices)

print "Gaussian Orthogonal Ensemble"
for n in [10,50,100,500,1000]:
    eigValues = []
    for i in range(1,101):
        matrix_size = n
        matrix = gaussianOrthogonalEnsemble(matrix_size)
        eighenValues = eigh(matrix, eigvals_only=True)
        data = []
        data.append(np.amin(eighenValues))
        data.append(np.amax(eighenValues))
        eigValues.append(data)
    
    wignerGaussian.update({n:eigValues})

print len(wignerGaussian)

#Min Values plotting
xValues = []
yValues = []
means = []
for x, y in sorted(bernoulliMatrices.items(), key=lambda s: s[0]):
    xValues.append(x)
    yValues_1 = []
    for z in y:
        yValues_1.append(z[0])
    yValues.append(yValues_1)
    means.append(np.mean(yValues_1))

plt.title("Bernoulli - Realizations of Eigen Min Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Min Values")
plt.plot(xValues, yValues, 'bo')
plt.show()
plt.close()

#With curve fitting
plt.title("Bernoulli - Realizations of Eigen Min Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Min Values")
plt.plot(xValues, yValues, 'bo')
plt.plot(xValues, means, '-r')
plt.show()
plt.close()


xValues = []
yValues = []
means = []
for x, y in sorted(wignerGaussian.items(), key=lambda s: s[0]):
    xValues.append(x)
    yValues_1 = []
    for z in y:
        yValues_1.append(z[0])
    yValues.append(yValues_1)
    means.append(np.mean(yValues_1))

plt.title("Gaussian - Realizations of Eigen Min Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Min Values")
plt.plot(xValues, yValues, 'bo')
plt.show()
plt.close()

plt.title("Gaussian - Realizations of Eigen Min Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Min Values")
plt.plot(xValues, yValues, 'bo')
plt.plot(xValues, means, '-r')
plt.show()
plt.close()


#Max Values plotting
xValues = []
yValues = []
means = []
for x, y in sorted(bernoulliMatrices.items(), key=lambda s: s[0]):
    xValues.append(x)
    yValues_1 = []
    for z in y:
        yValues_1.append(z[1])
    yValues.append(yValues_1)
    means.append(np.mean(yValues_1))

plt.title("Bernoulli - Realizations of Eigen Max Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Max Values")
plt.plot(xValues, yValues, 'bo')
plt.show()
plt.close()

#With curve fitting
plt.title("Bernoulli - Realizations of Eigen Max Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Max Values")
plt.plot(xValues, yValues, 'bo')
plt.plot(xValues, means, '-r')
plt.show()
plt.close()


xValues = []
yValues = []
means = []
for x, y in sorted(wignerGaussian.items(), key=lambda s: s[0]):
    xValues.append(x)
    yValues_1 = []
    for z in y:
        yValues_1.append(z[1])
    yValues.append(yValues_1)
    means.append(np.mean(yValues_1))

plt.title("Gaussian - Realizations of Eigen Max Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Max Values")
plt.plot(xValues, yValues, 'bo')
plt.show()
plt.close()

plt.title("Gaussian - Realizations of Eigen Max Values as a function of n")
plt.xlabel("Dimension")
plt.ylabel("Eigen Max Values")
plt.plot(xValues, yValues, 'bo')
plt.plot(xValues, means, '-r')
plt.show()
plt.close()



