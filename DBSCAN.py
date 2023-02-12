import math
import random
from matplotlib import pyplot as plt

def dis(p1, p2):
    distant = 0
    for index in range(len(p1)):
        distant += (p1[index]-p2[index])*(p1[index]-p2[index])
    return math.sqrt(distant)

class DBSCAN:
    def __init__(self):
        self.data = []
        self.radio = 0
        self.MinPts = 0
        self.Class = []

    def Train(self, data = [], radio = 0.2, MinPts = 5):
        self.data = data
        self.radio = radio
        self.MinPts = MinPts
        CoreObjects = []
        vis = []
        for i in range(len(data)):
            vis.append(False)
            num = 0
            for j in range(len(data)):
                distant = dis(data[i], data[j])
                if distant < self.radio:
                    num += 1
            if num >= self.MinPts:
                CoreObjects.append(i)
        while True:
            if len(CoreObjects) == 0:
                break
            pos = random.randint(0, len(CoreObjects)-1)
            index = CoreObjects[pos]
            c = [index]
            vis[index] = True
            for i in range(len(data)):
                if vis[i]:
                    continue
                for j in range(len(c)):
                    if dis(data[c[j]], data[i]) <= self.radio:
                        c.append(i)
                        check = True
                        vis[i] = True
                        break
            self.Class.append(c)
            #从核心元素总去除c中的元素
            for item in c:
                if item in CoreObjects:
                    CoreObjects.pop(CoreObjects.index(item))

    def ShowPlt(self):
        marks = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        for i in range(len(self.Class)):
            for item in self.Class[i]:
                plt.plot(self.data[item][0], self.data[item][1], marks[i], markersize=5)
        plt.show()

if __name__ == "__main__":
    dbscan = DBSCAN()
    datas = [[0.697, 0.460], [0.774, 0.376], [0.634, 0.264], [0.608, 0.318],
             [0.556, 0.215], [0.403, 0.237], [0.481, 0.149], [0.437, 0.211],
             [0.666, 0.091], [0.243, 0.267], [0.245, 0.057], [0.343, 0.099],
             [0.639, 0.161], [0.657, 0.198], [0.360, 0.370], [0.593, 0.042],
             [0.719, 0.103], [0.359, 0.188], [0.339, 0.241], [0.282, 0.257],
             [0.748, 0.232], [0.714, 0.346], [0.483, 0.312], [0.478, 0.437],
             [0.525, 0.369], [0.751, 0.489], [0.532, 0.472], [0.473, 0.376],
             [0.725, 0.445], [0.446, 0.459]]
    dbscan.Train(radio=0.11, data=datas)
    dbscan.ShowPlt()