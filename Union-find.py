class UnionFind:
    def __init__(self):
        self.holder = []

    def createSet(self, value):
        table = {}
        table[value] = value
        self.holder.append(table)

    def find(self, value):
        for sets in self.holder:
            if value in sets:
                return sets[value]
        return None

    def union(self, valueOne, valueTwo):
        find1 = self.find(valueOne)
        find2 = self.find(valueTwo)
        if find1 is None or find2 is None:
            return
        idx = 0
        idx2 = 0
        for i in range(len(self.holder)):
            if valueOne in self.holder[i]:
                idx = i
            if valueTwo in self.holder[i]:
                idx2 = i
        if idx == idx2:
            return
        value = self.holder[idx][valueOne]
        for keys in self.holder[idx2].keys():
            self.holder[idx][keys] = value
        self.holder.pop(idx2)