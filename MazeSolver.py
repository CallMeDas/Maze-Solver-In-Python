

from collections import deque
import heapq

maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
]

start = (0, 1)
goal = (6, 2)

# DFS Algorithm...
def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set() 
    while stack:
        (vertex, path) = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == goal:
            return path
        for next in get_neighbors(maze, vertex):
            if next not in visited:
                stack.append((next, path + [next])) 
    return None


# BFS Algorithm...
def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()  
    while queue:
        (vertex, path) = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        for next in get_neighbors(maze, vertex):
            if next == goal:
                return path + [next]
            if next not in visited:
                queue.append((next, path + [next]))
    return None  


# Uniform Cost Search Algorithm...
def ucs(maze, start, goal):
    queue = [(0, start, [start])]
    heapq.heapify(queue)
    visited = set()
    while queue:
        (cost, vertex, path) = heapq.heappop(queue)
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == goal:
            return path
        for next in get_neighbors(maze, vertex):
            if next not in visited:
                heapq.heappush(queue, (cost + 1, next, path + [next]))
    return None


# A*  Algorithm...
def a_star(maze, start, goal):
    queue = [(0 + manhattan_distance(start, goal), 0, start, [start])]
    heapq.heapify(queue)
    visited = set()
    while queue:
        (priority, cost, vertex, path) = heapq.heappop(queue)
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == goal:
            return path
        for next in get_neighbors(maze, vertex):
            if next not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan_distance(next, goal)
                heapq.heappush(queue, (priority, new_cost, next, path + [next]))
    return None  


# Best-First-Search Algorithm...
def best_first_search(maze, start, goal):
    queue = [(manhattan_distance(start, goal), start, [start])]
    heapq.heapify(queue)
    while queue:
        (priority, vertex, path) = heapq.heappop(queue)
        for next in get_neighbors(maze, vertex):
            if next == goal:
                return path + [next]
            else:
                heapq.heappush(queue, (manhattan_distance(next, goal), next, path + [next]))
    return None


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(maze, position):
    neighbors = []
    x, y = position
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def print_maze(maze, path=None):
    if path is None:
        print("No path found.")
    else:
        print("Path Found: ")
        for i, row in enumerate(maze):
            for j, col in enumerate(row):
                if (i, j) == start:
                    print("S", end=" ")
                elif (i, j) == goal:
                    print("G", end=" ")
                elif path and (i, j) in path:
                    print("-", end=" ")
                else:
                    print("1" if col == 1 else "0", end=" ")
            print()




while True:
    print("\nMaze Solver Options:")
    print("1. DFS")
    print("2. BFS")
    print("3. UCS")
    print("4. A*")
    print("5. Best-First-Search")
    print("6. Exit")
    try:
        choice = int(input("\nEnter your choice between 1 and 6: "))
        match(choice):
            case 1:
                print_maze(maze, dfs(maze, start, goal))
            case 2:
                print_maze(maze, bfs(maze, start, goal))
            case 3:
                print_maze(maze, ucs(maze, start, goal))
            case 4:
                print_maze(maze, a_star(maze, start, goal))
            case 5:
                print_maze(maze, bfs(maze, start, goal))
            case 6:
                break
            case _ :
                print("Invalid Number... Please choose between 1 and 6.")
        again = input('Solve Again y or n: ')
        if again.lower() != 'y':
            print("Closing the Program...")
            break
    except:
        print("Invalid input...")
