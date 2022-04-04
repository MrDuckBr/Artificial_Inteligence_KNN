from copy import deepcopy
from ctypes import sizeof
from hashlib import new
from random import random, shuffle
from unicodedata import category
import pandas as pd
import csv
from knn import Knn


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


def init(filepath):
    datas = readDocument(filepath=filepath)
    createTestList(datas)

# Precisa ver uma forma de randomizar essa lista aqui para ter o teste


def createTestList(data, randomValue=0.3):
    # Shuffle na lista
    newData = random.shuffle(data)
    # print(data)
    # criando uma lista com apenas a porcentagem da nova lista
   # newData = deepcopy(newData[:int(len(newData)*randomValue)])
