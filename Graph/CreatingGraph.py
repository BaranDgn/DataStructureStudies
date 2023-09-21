# Graph

class Graph:
    def __init__(self):
        self.adjDic = {}

    def addVertex(self, vertex):
        if vertex not in self.adjDic.keys():
            self.adjDic[vertex] = []
            return True  # eklendi mi diye görebilmek icin yapılır
        return False

    def addEdge(self, v1, v2):
        if v1 in self.adjDic.keys() and v2 in self.adjDic.keys():
            self.adjDic[v1].append(v2)
            self.adjDic[v2].append(v1)
            return True
        return False

    def removeEdge(self, v1, v2):
        if v1 in self.adjDic.keys() and v2 in self.adjDic.keys():
            try:
                self.adjDic[v1].remove(v2)
                self.adjDic[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjDic.keys():
            for relatedVertex in self.adjDic[vertex]:  #  çıkarılmak istenen vertex in baglı oldugu vertex lerdeki yerlerinde de cıkarılması için
                self.adjDic[relatedVertex].remove(vertex)
            del self.adjDic[vertex]

    def printGraph(self):
        for vertex in self.adjDic:
            print(vertex, "->", self.adjDic[vertex])


graph = Graph()
graph.addVertex("IST")
graph.addVertex("AMS")
graph.addVertex("CDG")
graph.addVertex("JFK")

graph.addEdge("IST", "AMS")
graph.addEdge("IST", "CDG")
graph.addEdge("IST", "JFK")
graph.addEdge("AMS", "CDG")
graph.addEdge("AMS", "JFK")
graph.addEdge("CDG", "JFK")

graph.printGraph()

print()

graph.removeVertex("JFK")
graph.removeEdge("IST", "CDG")
graph.removeEdge("CDG", "JFK")
graph.printGraph()
