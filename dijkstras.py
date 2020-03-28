#This is a weighted graph algorithm.
#By using this algorithm, you can figure out what is the shortest path for a weighted graph. Therefore letting you find the fastest path.
#Learn what cycles are in graphs.
#Terminology:
#Each Edge in a Dijkstra Algorithm get assigned a Weight, this makes it a weighted graph
#To calculate the shortest path in a unweighted graph, use breadth-first search.
#Dijkstra only works with directed acylclic graphs - DAGs for short
#Djikstras DOES NOT work with negative weighted edges. Look at Bellman-Ford algorithm calcualte a graph with negative weights

infinity = float("inf")
graph ={}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] ={}
graph["a"]["end"] =1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["end"]=5

graph["end"]={}

costs ={}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

parents ={}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []


def Dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node



Dijkstra()