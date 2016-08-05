import numpy as np


def emptyRelation(n):
    relation = np.zeros((n, n), dtype=np.int)
    relation = np.matrix(relation)
    return relation

def universalRelation(n):
    relation = np.ones((n, n), dtype=np.int)
    relation = np.matrix(relation)
    return relation

def equalityRelation(n):
    relation = np.identity(n, dtype=np.int)
    relation = np.matrix(relation)
    return relation

def notEqualRelation(n):
    universalRelation = np.ones((n, n), dtypes=np.int)
    equalityRelation = np.identity(n, dtype=np.int)
    notEqual = np.subtract(universalRelation, equalityRelation)
    return notEqual

def greaterThanRelation(n):
    zeroRelation = np.zeros((n, n), dtype=np.int)
    for yCount in range(n):
        for xCount in range(n):
            if xCount < yCount:
                np.put(zeroRelation, zeroRelation[xCount, yCount], [1])
    zeroRelation = np.matrix(zeroRelation)

def lessThanRelation(n):
    zeroRelation = np.zeros((n, n), dtype=np.int)
    for yCount in range(n):
        for xCount in range(n):
            if xCount > yCount:
                np.put(zeroRelation, zeroRelation[xCount, yCount], [1])
    zeroRelation = np.matrix(zeroRelation)

def greaterThanOrEqualRelation(n):
    greaterThanArray = np.array(greaterThanRelation(n))
    equalityArray = np.identity(n, dtype=np.int)
    finalProduct = np.add(greaterThanArray, equalityArray)
    return finalProduct

def lessThanOrEqualRelation(n):
    lessThanArray = np.array(lessThanRelation(n))
    equalityArray = np.identity(n, dtype=np.int)
    finalProduct = np.add(lessThanArray, equalityArray)
    return finalProduct