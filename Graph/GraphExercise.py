# GRAPH EXERCISE

class GraphExe:
    def __init__(self):
        self.gDic = {}

    def addingVertexToList(self, vertex):
        if vertex not in self.gDic.keys():
            self.gDic[vertex] = {}
            return True
        return False

    def addingEdgeToList(self, v1, v2, weight):
        if v1 in self.gDic.keys() and v2 in self.gDic.keys():
            self.gDic[v1][v2] = weight
            self.gDic[v2][v1] = weight
            return True
        return False


class RemovingGraph:
    def __init__(self, graph):
        self.graph = graph

    def removeVertex(self, vertex):
        if vertex in self.graph.gDic.keys():
            # Remove the vertex and its associated edges
            del self.graph.gDic[vertex]

            # Remove references to the removed vertex from other vertices
            for other_vertex in self.graph.gDic:
                if vertex in self.graph.gDic[other_vertex]:
                    del self.graph.gDic[other_vertex][vertex]

    def removeEdge(self, v1, v2):
        if v1 in graph.gDic.keys() and v2 in graph.gDic.keys():
            try:
                del self.graph.gDic[v1][v2]
                del self.graph.gDic[v2][v1]
            except ValueError:
                pass
            return True
        return False


class PrintingGraph:
    def __init__(self, graph):
        self.graph = graph

    def printGraph(self):
        for vertex in self.graph.gDic:
            print(vertex, "->", self.graph.gDic[vertex])

    def printGraph2(self):
        for vertex in self.graph.gDic:
            neighbor_str = ", ".join(f"{neighbor}({weight})" for neighbor, weight in self.graph.gDic[vertex].items())
            print(f"{vertex} -> {neighbor_str}")


class SearchFlight:
    def __init__(self, graph):
        self.graph = graph

    def searchForFlight(self, departure, arrival):
        flights = []
        if departure in self.graph.gDic.keys():
            for arrive in self.graph.gDic[departure].keys():
                if arrive == arrival:
                    flight_info = {
                        "departure": departure,
                        "arrival": arrive,
                        "price": self.graph.gDic[departure][arrive]
                    }
                    flights.append(flight_info)
                return flights

    def searchForAllFlight(self, departure, arrival):
        flights = []
        total = 0
        if departure in self.graph.gDic.keys():
            # IST - AMS
            for arrive in self.graph.gDic[departure].keys():

                for transfer_flight in self.graph.gDic[arrive].keys():
                    if transfer_flight == arrival:
                        total += self.graph.gDic[arrive][transfer_flight]
                        flight_info = {
                            "departure": departure + " - " + arrive,
                            "arrival": arrival,
                            "price": int(total + self.graph.gDic[departure][arrive])
                        }
                        flights.append(flight_info)
                if arrive == arrival:
                    flight_info = {
                        "departure": departure,
                        "arrival": arrival,
                        "price": self.graph.gDic[departure][arrive]
                    }
                    flights.append(flight_info)
                total = 0
            return flights


class OptimumJourney:
    def __init__(self, graph, searchFlight):
        self.graph = graph
        self.searchFlight = searchFlight

    def optimumTicket(self, departure, arrival):
        allFlights = searchFlight.searchForAllFlight(departure, arrival)
        optimumPrice = float('inf')  # Initialize to positive infinity to ensure any price is lower
        optimumFlight = []
        for flight in allFlights:
            price = flight.get("price", float('inf'))
            if price < optimumPrice:
                optimumPrice = price

        if optimumPrice == float('inf'):
            return "No flights found"
        else:
            return optimumPrice



graph = GraphExe()
output = PrintingGraph(graph)
removeGraph = RemovingGraph(graph)
searchFlight = SearchFlight(graph)
optJourney = OptimumJourney(graph, searchFlight)

graph.addingVertexToList("IST")
graph.addingVertexToList("AMS")
graph.addingVertexToList("CDG")
graph.addingVertexToList("JFK")

graph.addingEdgeToList("IST", "AMS", 100)
graph.addingEdgeToList("IST", "CDG", 200)
graph.addingEdgeToList("IST", "JFK", 50)
graph.addingEdgeToList("AMS", "CDG", 60)
graph.addingEdgeToList("AMS", "JFK", 10)
graph.addingEdgeToList("CDG", "JFK", 80)


print("The Optimum price for flight is", optJourney.optimumTicket("IST", "AMS"))
# output.printGraph()
# removeGraph.removeVertex("IST")
# removeGraph.removeEdge("IST", "AMS")
print(searchFlight.searchForFlight("IST", "AMS"))
# searchFlight.searchForFlight("CDG", "JFK")
print(searchFlight.searchForAllFlight("IST", "AMS"))
print(searchFlight.searchForAllFlight("AMS", "JFK"))

"""
departure_city = "IST"
arrival_city = "AMS"
result = searchFlight.searchForFlight(departure_city, arrival_city)
if result:
    for flight in result:
        print(f"Flight from {flight['departure']} to {flight['arrival']} - Price: {flight['price']}")
else:
    print(f"No flights found from {departure_city} to {arrival_city}")
"""

print("----------------")
output.printGraph()
print("----------------")
output.printGraph2()
