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