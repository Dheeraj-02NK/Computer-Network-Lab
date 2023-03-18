import heapq  # heapq is used to implement priority queues

def dijkstra(graph, start):
    # initialize all distances to infinity
    distances = {node: float('inf') for node in graph}
    # set the distance to the start node to 0
    distances[start] = 0
    # initialize the priority queue with the start node and its distance
    pq = [(0, start)]
    
    # loop while there are still nodes to visit
    while pq:
        # pop the node with the smallest distance from the priority queue
        (dist, node) = heapq.heappop(pq)
        # if the distance to the node is already known, skip it
        if dist > distances[node]:
            continue
        # loop over the node's neighbors
        for neighbor, weight in graph[node].items():
            # calculate the distance to the neighbor through the current node
            distance = dist + weight
            # if this distance is shorter than the previously known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # add the neighbor to the priority queue with its new distance
                heapq.heappush(pq, (distance, neighbor))
    
    # return the dictionary of shortest distances from the start node to each node
    return distances
  
  graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'C': 7, 'D': 5},
    'C': {'D': 2, 'E': 7},
    'D': {'E': 1},
    'E': {}
}

distances = dijkstra(graph, 'A')
print(distances)
