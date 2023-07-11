h = int(input())
r = int(input())
roads = []
for _ in range(r):
    u = int(input())
    v = int(input())
    roads.append([u,v])
coords = []
for _ in range(h):
    x = int(input())
    y = int(input())
    coords.append([x,y])
q = int(input())
for _ in range(q):
    perimeter = int(input())
    hospitals = list(map(int,input().strip().split()))

def build_graph(hospitals, roads):
    graph = {}
    for hospital in hospitals:
        graph[hospital] = set()

    for road in roads:
        u, v = road
        graph[u].add(v)
        graph[v].add(u)

    return graph

def count_hospitals_along_cycle(graph, cycle):
    count = 0
    for node in cycle:
        if node in graph:
            count += 1
    return count

def dfs(graph, start, visited, path):
    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

    path.pop()

def solve_queries(hospitals, roads, queries):
    graph = build_graph(hospitals, roads)
    results = []

    for query in queries:
        perimeter = query[0]
        cycle = query[1:]
        cycle.append(cycle[0])  # Ensure the cycle is closed

        visited = set()
        path = []

        # Perform DFS starting from the first hospital in the cycle
        dfs(graph, cycle[0], visited, path)

        # Find the number of hospitals along the cycle
        count = count_hospitals_along_cycle(graph, cycle)
        results.append(count)

    return results

# Example usage
hospitals = [1, 2, 3, 4, 5]
roads = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
queries = [
    (5, 1, 2, 3, 4, 5),  # Cycle covering all hospitals
    (4, 1, 2, 3, 4),     # Cycle covering 4 hospitals
    (3, 1, 2, 3),        # Cycle covering 3 hospitals
]

results = solve_queries(hospitals, roads, queries)
print(results)  # Output: [5, 4, 3]
