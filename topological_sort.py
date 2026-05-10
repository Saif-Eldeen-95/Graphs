from collections import deque
def topological_sort(graph, vertices):
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    order = []
    visited_edges = 0  
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            visited_edges += 1  
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    total_edges = sum(len(graph[u]) for u in graph)
    return order if visited_edges == total_edges else None