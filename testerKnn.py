# base
# https://github.com/thiagopnobre/knn/blob/8cef99bdb227cfddb688df01d2cba1dc0480cd01/K-NN.py#L17
from cgi import test
from copy import deepcopy
from ctypes import sizeof
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


def init(filepath, k):
    datas = readDocument(filepath=filepath)
    # Retorna a lista de teste e a lista de treino, que são KNN's
    testList, trainingList = createTestList(datas)
    findMinusDistance(dataTest=testList, dataTraining=trainingList, k=k)
# Precisa ver uma forma de randomizar essa lista aqui para ter o teste


def createTestList(data, randomValue=0.3):
    # Shuffle na lista
    testValues = []
    trainingValues = []

    for knnElements in data:
        if random() < randomValue:
            testValues.append(knnElements)
        else:
            trainingValues.append(knnElements)

    return (testValues, trainingValues)

    # Aqui vou conferir todas as distancias para todos e adicionar ao TestData.py
    # # apos isso fazer a verificação dos mais proximos, junto ao K fornecido pelo professor


# data training = 80% dos dados
def findMinusDistance(dataTest, dataTraining, k):
    listofMinusDistance = []
   # print('findMinusDistance \n')
    for lineTest in dataTest:

        perLineSum = sumLine(lineTest.values)
        listofMinusDistance.append(findMinusDistancePerLine(
            line=perLineSum, dataTraining=dataTraining, k=k))
    print(listofMinusDistance)
    return 0


def sumLine(line):
    amount = 0
    for l in line:
        amount += l
    return amount


def findMinusDistancePerLine(line, dataTraining, k):
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
    print('distance ', _distance)
    return (_distance**0.5)
