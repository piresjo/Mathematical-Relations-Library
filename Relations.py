import numpy
import itertools
import math

def numberOfTransitive(n):
    if n < 1 or n > 4:
        return -1
    
    numberList = list(itertools.product([0, 1], repeat = n ** 2))
    count = 0
    totalNumber = 2 ** (n ** 2)
    listCount = 0
    if n == 1:
        while (listCount < totalNumber):
            extractList = numberList[listCount]
            testMatrix = numpy.matrix([extractList[0]])
            if  testTransitive(testMatrix):
                count += 1
            listCount += 1
    if n == 2:
        while (listCount < totalNumber):
            extractList = numberList[listCount]
            testMatrix = numpy.matrix([[extractList[0], extractList[1]], \
                                       [extractList[2], extractList[3]]])

            if testTransitive(testMatrix):
                count += 1
            listCount += 1
    if n == 3:
        while (listCount < totalNumber):
            extractList = numberList[listCount]
            testMatrix = numpy.matrix([[extractList[0], extractList[1], extractList[2]], \
                                       [extractList[3], extractList[4], extractList[5]], \
                                       [extractList[6], extractList[7], extractList[8]]])
            
            if testTransitive(testMatrix):
                count += 1
            listCount += 1
    if n == 4:
        while (listCount < totalNumber):
            extractList = numberList[listCount]
            testMatrix = numpy.matrix([[extractList[0], extractList[1], extractList[2], extractList[3]], \
                                       [extractList[4], extractList[5], extractList[6], extractList[7]], \
                                       [extractList[8], extractList[9], extractList[10], extractList[11]], \
                                       [extractList[12], extractList[13], extractList[14], extractList[15]]])           

            if testTransitive(testMatrix):
                count += 1
            listCount += 1
    return count
    
def modifyMatrix(matrixToModify, n):
    arrayToModify = numpy.array(matrixToModify)
    arrayToModify[arrayToModify > 1] = 1
    matrixToModify = numpy.matrix(arrayToModify)
    return matrixToModify
            

def lessThanOrEqual(booleanMultipliedMatrix, originalMatrix, n):
    topVal = n ** 2
    counter = 0
    while (counter < topVal):
        if booleanMultipliedMatrix.item(counter) > originalMatrix.item(counter):
            return False
        counter += 1
    return True

def calculateSterlingSecondKind(n, k):
    finalProduct = 0
    if n == 0 and k == 0:
        return 1
    if n == 0 and k != 0:
        return 0
    j = 0
    while j <= k:
        combinationVal = math.factorial(k) / (math.factorial(j) * math.factorial(k - j))
        addingPart = ((-1) ** (k - j)) * combinationVal * (j ** n)
        finalProduct = finalProduct + addingPart
        j += 1
    finalProduct = finalProduct / math.factorial(k)
    return finalProduct

def combinatoricsSymmetric(n):
    exponent = (n ** 2) + n
    exponent = exponent / 2
    return 2 ** exponent

def combinatoricsAntisymmetric(n):
    firstExponent = n * (n -1)
    firstExponent = firstExponent / 2
    secondExponent = n
    result = (3 ** firstExponent) * (2 ** secondExponent)
    return result
    
def combinatoricsReflexiveOrIrreflexive(n):
    exponent = (n ** 2) - n
    return 2 ** exponent
    
def combinatoricsEquivalence(n):
    finalProduct = 0
    k = 1
    while (k <= n):
        sterVal = calculateSterlingSecondKind(n, k)
        finalProduct = finalProduct + sterVal
        k += 1
    return finalProduct
    
def testReflexive(matrix):
    size = matrix.shape
    if size[0] != size[1]:
        return False
    if size[0] == size[1]:
        identityMatrix = numpy.matrix(numpy.identity(size[0]))
        if (lessThanOrEqual(identityMatrix, matrix, size[0])):
            return True
        return False

def testIrreflexive(matrix):
    size = matrix.shape
    if size[0] != size[1]:
        return False
    if size[0] == size[1]:
        identityMatrix = numpy.identity(size[0])
        identityMatrix - numpy.matrix(identityMatrix)
        topVal = size[0] ** 2
        counter = 0
        while (counter < topVal):
            if matrix.item(counter) == 1 and identityMatrix.item(counter) == 1:
                return False
            counter += 1
        return True

def testSymmetric(matrix):
    size = matrix.shape
    if size[0] != size[1]:
        return False
    if size[0] == size[1]:
        inputArray = numpy.array(matrix)
        if numpy.array_equal(inputArray, inputArray.T):
            return True
        return False

def testAntisymmetric(matrix):
    size = matrix.shape 
    if size[0] != size [1]:
        return False
    if size[0] == size[1]:

        inputArray = numpy.array(matrix)
        transposeArray = inputArray.T
        transposeMatrix = numpy.matrix(transposeArray)
        identityArray = numpy.identity(size[0])
        identityMatrix = numpy.matrix(identityArray)
        finalProduct = numpy.arange(size[0] ** 2)
        topVal = size[0] ** 2
        counter = 0
        
        while (counter < topVal):
            replaceVal = finalProduct.item(counter)
            if matrix.item(counter) == 1 and transposeMatrix.item(counter) == 1:
                numpy.put(finalProduct, [replaceVal], [1])
            else:
                numpy.put(finalProduct, [replaceVal], [0])
            counter += 1
            
        finalMatrix = numpy.matrix(finalProduct)
                
        
        if lessThanOrEqual(finalMatrix, identityMatrix, size[0]):
            return True
        return False

def testTransitive(matrix):
    size = matrix.shape
    if size[0] != size[1]:
        return False
    if size[0] == size[1]:
        multipliedMatrix = matrix * matrix
        multipliedMatrix = modifyMatrix(multipliedMatrix, size[0])
        if lessThanOrEqual(multipliedMatrix, matrix, size[0]):
            return True
        return False

def testEquivalence(matrix):
    if testReflexive(matrix) and testSymmetric(matrix) and testTransitive(matrix):
        return True
    return False

def testPartialOrder(matrix):
    if testReflexive(matrix) and testAntisymmetric(matrix) and testTransitive(matrix):
        return True
    return False

def reflexiveClosure(matrix):
    size = matrix.shape
    if size[0] != size[1]:
        return None
    if size[0] == size[1]:
        finalProduct = numpy.arange(size[0] ** 2)
        identityMatrix = numpy.identity(size[0], dtype = numpy.int)
        identityMatrix = numpy.matrix(identityMatrix)
        counter = 0
        topVal = size[0] ** 2
        while (counter < topVal):
            replaceVal = finalProduct.item(counter)
            if matrix.item(counter) == 0 and identityMatrix.item(counter) == 0:
                numpy.put(finalProduct, [replaceVal], [0])
            else:
                numpy.put(finalProduct, [replaceVal], [1])
            counter += 1
        finalProduct = finalProduct.reshape(size[0], size[0])   
        finalMatrix = numpy.matrix(finalProduct)
        return finalMatrix

def symmetricClosure(matrix):
    size = matrix.shape
    if size[0] != size[1]:
        return None
    if size[0] == size[1]:
        finalProduct = numpy.arange(size[0] ** 2)
        inputArray = numpy.array(matrix)
        transposeMatrix = numpy.matrix(inputArray.T)
        counter = 0
        topVal = size[0] ** 2
        while (counter < topVal):
            replaceVal = finalProduct.item(counter)
            if matrix.item(counter) == 0 and transposeMatrix.item(counter) == 0:
                numpy.put(finalProduct, [replaceVal], [0])
            else:
                numpy.put(finalProduct, [replaceVal], [1])
            counter += 1
        finalProduct = finalProduct.reshape(size[0], size[0])
        finalMatrix = numpy.matrix(finalProduct)
        return finalMatrix
