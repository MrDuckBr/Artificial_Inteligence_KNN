class Knn:
    def __init__(self, values, category):
        self.values = values
        self.category = category
        self.neighborhood = []

    def _neighborhood(self, values):
        self.neighborhood.append(values)
