import heapq

def prims_mst(graph, start):
    visited      = set()
    min_heap     = [(0, start, None)]
    mst_edges    = []
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total_weight += weight
        if parent is not None:
            mst_edges.append((parent, node, weight))
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    if len(visited) != len(graph):
        raise ValueError(f"Graph not fully connected.")

    return mst_edges, total_weight