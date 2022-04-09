class Knn:
    def __init__(self, values, category):
        self.values = values
        self.category = category
        self.neighbors = []

    def setNeighbors(self, listOfValues):
        self.neighbors = listOfValues


class DistanceKNN:
    def __init__(self, element, distanceList, trainingList):
        self.element = element
        self.distanceList = distanceList
        self.trainingList = trainingList
