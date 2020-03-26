import numpy as np
import pickle

#This method pads the input array with several -1s to prevent against null pointer exceptions
#It then finds the neighboring values of a particular value in the input array and filters out all the values that are -1
def returnNeighbors(arr, row, column):
    neighbors = []
    paddedArr = np.pad(arr, pad_width = 1, mode = 'constant', constant_values = -1)
    actualRow = row + 1
    actualCol = column + 1
    neighbors.append(paddedArr[actualRow + 1][actualCol])
    neighbors.append(paddedArr[actualRow][actualCol + 1])
    neighbors.append(paddedArr[actualRow + 1][actualCol + 1])
    neighbors.append(paddedArr[actualRow - 1][actualCol])
    neighbors.append(paddedArr[actualRow][actualCol - 1])
    neighbors.append(paddedArr[actualRow - 1][actualCol - 1])
    neighbors.append(paddedArr[actualRow - 1][actualCol + 1])
    neighbors.append(paddedArr[actualRow + 1][actualCol - 1])
    boolArray = neighbors != -1
    npNeighborsArray = np.asarray(neighbors)
    toReturn = np.extract(npNeighborsArray != -1, npNeighborsArray)
    return toReturn

def returnNextGen(arr):
    numRows = np.shape(arr)[0]
    numCols = np.shape(arr)[1]
    nextGen = np.zeros((numRows, numCols), dtype = int)
    for i in range(0, numRows):
        for j in range(0, numCols):
            neighborValues = returnNeighbors(arr, i, j)
            if (arr[i][j] == 0):
                if (np.shape(np.extract(neighborValues == 1, neighborValues))[0] == 3):
                    nextGen[i][j] = 1
            else:
                if (np.shape(np.extract(neighborValues == 1, neighborValues))[0] == 3 or np.shape(np.extract(neighborValues == 1, neighborValues))[0] == 2):
                    nextGen[i][j] = 1
    
    return nextGen

def playGame(generations, fileName):
    startingArr = pickle.load(open(fileName, 'rb'))
    for i in range(0, generations):
        startingArr = returnNextGen(startingArr)
    return startingArr



    


    