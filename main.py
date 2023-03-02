from queue import PriorityQueue
import math

def euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities"""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def a_star(origin, destination, adjacencies):
    visited = set()  # visited nodes
    frontier = PriorityQueue()  # priority queue of nodes to visit
    frontier.put((0, origin, None))  # origin to the frontier

    while not frontier.empty():
        _, current, parent = frontier.get()  # get the smallest value node
        if current == destination:
            path = [current]
            while parent is not None:
                path.append(parent)
                _, parent = visited[parent]
            return path[::-1]  # return the reversed path from origin to destination

        visited.add((current, parent))  # current node as visited
        for neighbor in adjacencies[current]:
            if neighbor not in visited:
                cost = euclidean_distance(origin, neighbor) + euclidean_distance(neighbor, destination)
                frontier.put((cost, neighbor, current))

    return None  # return none if the destination cannot be reached
