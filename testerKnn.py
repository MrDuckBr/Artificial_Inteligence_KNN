# base
# https://github.com/thiagopnobre/knn/blob/8cef99bdb227cfddb688df01d2cba1dc0480cd01/K-NN.py#L17
from calendar import calendar
from cgi import test
from copy import deepcopy
from ctypes import sizeof
from errno import ENAMETOOLONG
from hashlib import new
from math import dist
from random import Random, random, shuffle
from turtle import distance
from unicodedata import category
import pandas as pd
import csv
from knn import Knn


# Global values
categoryCount = []


def readDocument(filepath):
    datasWithoutLastValor = []

    file = csv.reader(open(filepath, "r"))
    for row in file:
        category = row[-1]
        if len(row) != 0:
            params = []
            for i in range(len(row)-1):
                params.append(float(row[i]))
            knn = Knn(values=params, category=category)
            datasWithoutLastValor.append(knn)

    return(datasWithoutLastValor)


def createTestList(data, randomValue=0.3):
    # Shuffle na lista
    trainingValues = []
    testValues = []

    for knnElements in data:
        if random() < randomValue:
            trainingValues.append(knnElements)
        else:
            testValues.append(knnElements)

    return (testValues, trainingValues)


def findMinusDistance(training, test):
    listofMinusDistance = []

    for lineTest in test:
        # Calculcar aqui nesse ponto os vizinhos e a distancia, como manter o indice ?
        lineTest.setNeighborsDistance()  # aqui coloca a lista da distancia
        # aqui coloca a lista que foi utilizada
        lineTest.setNeighbors(training)
        # To perdido aqui vei, que bosta

        listofMinusDistance.append(list(findMinusDistancePerLine(
            line=perLineSum, dataTraining=dataTraining)))

    print(listofMinusDistance)

    return listofMinusDistance


def sumLine(line):
    amount = 0
    for l in line:
        amount += l
    return amount


def findMinusDistancePerLine(line, dataTraining):
    _distanceSum = []
   # print('findMinusDistancePerLine \n')
    for lineTraining in dataTraining:
        _distanceSum.append(euclidianDistance(
            lineTest=line, lineTraining=lineTraining))


# Nesse ponto retorna uma lista, correto?
    return _distanceSum


def euclidianDistance(lineTest, lineTraining):
   # print('euclidianDistance \n')
    amountTrainingData = sumLine(line=lineTraining.values)
    _distance = (lineTest-amountTrainingData)**2
   # print('distance ', _distance)
    return (_distance**0.5)


def init(filepath, k):
    datas = readDocument(filepath=filepath)
    # Retorna a lista de teste e a lista de treino, que são KNN's
    testList, trainingList = createTestList(datas)
    searchDistance = findMinusDistance(training=trainingList, test=testList)
    distanceValues = findMinusDistance(
        dataTest=testList, dataTraining=trainingList)
