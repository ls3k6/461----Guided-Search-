from queue import PriorityQueue
import math

def euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities"""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def a_star(origin, destination, adjacencies):
    visited = set()  # Set of visited nodes
    frontier = PriorityQueue()  # Priority queue of nodes to visit
    frontier.put((0, origin, None))  # Add the origin to the frontier

    while not frontier.empty():
        _, current, parent = frontier.get()  # Get the node with the smallest heuristic value
        if current == destination:
            path = [current]
            while parent is not None:
                path.append(parent)
                _, parent = visited[parent]
            return path[::-1]  # Return the reversed path from origin to destination

        visited.add((current, parent))  # Mark the current node as visited
        for neighbor in adjacencies[current]:
            if neighbor not in visited:
                cost = euclidean_distance(origin, neighbor) + euclidean_distance(neighbor, destination)
                frontier.put((cost, neighbor, current))  # Add the neighbor to the frontier with its heuristic value

    return None  # Return None if the destination cannot be reached
