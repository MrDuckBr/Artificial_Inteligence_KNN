# base
# https://github.com/thiagopnobre/knn/blob/8cef99bdb227cfddb688df01d2cba1dc0480cd01/K-NN.py#L17
from calendar import calendar
from cgi import test
from copy import deepcopy
from ctypes import sizeof
from errno import ENAMETOOLONG
from hashlib import new
from math import dist
from multiprocessing.sharedctypes import Value
from optparse import Values
from random import Random, random, shuffle
from turtle import distance
from unicodedata import category
import pandas as pd
import csv
from knn import DistanceKNN, Knn


# Global values
categoryCount = []


def init(filepath, k):
    datas = readDocument(filepath=filepath)
    # Retorna a lista de teste e a lista de treino, que são KNN's
    # a menor quantidade esta na training values
    testList, trainingList = createTestList(datas)

   # aqui temos uma lista de KNN distance
    distanceTeste = findMinusDistance(training=trainingList, test=testList)
    distanceSorted(distanceTeste)
    # Depois de ordenar so falta comparar com as distancias e ver o K pra ver se é o mesmo


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
    listofDistanceKNN = []

    for lineTest in test:  # aqui eu tenho cada linha do teste
        # Nesse ponto eu tenho cada teste
        # e preciso que ele saiba a distancia de todos os treinos
        # Como armazenar ???????????
        euclidianList = findMinusDistancePerLine(
            line=lineTest, dataTraining=training)
        listofDistanceKNN.append(DistanceKNN(
            element=lineTest, trainingList=training, distanceList=euclidianList))

   # print(listofMinusDistance)

    return listofDistanceKNN


def findMinusDistancePerLine(line, dataTraining):
    array = []
   # print('findMinusDistancePerLine \n')
    for lineTraining in dataTraining:
        array.append(euclidianDistance(
            lineTest=line, lineTraining=lineTraining))
    return array


def euclidianDistance(lineTest, lineTraining):
   # print('euclidianDistance \n')

    _distance = ((lineTraining.values[0]-lineTest.values[0])
                 ** 2) + ((lineTraining.values[2]-lineTest.values[2])**2)
   # print('distance ', _distance)
    return (_distance**0.5)

# Falta essa porra aqui


def distanceSorted(distanceTest):
    for line in distanceTest:
        print(line.trainingList)
      #  distanceList, trainingList = (list(t) for t in zip(
       #     *sorted(zip(line.distanceList, line.trainingList))))

    # return distanceList, trainingList
