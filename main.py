from Graph import bfs, dfs
from topological_sort import topological_sort
from mst import prims_mst


print("=== BFS / DFS ===")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}
print("BFS:", bfs(graph, 'A'))
print("DFS:", dfs(graph, 'A'))

graph = {
    1:  [2, 3],
    2:  [1, 4, 5],
    3:  [1, 6, 7],
    4:  [2, 8],
    5:  [2, 8],
    6:  [3, 9],
    7:  [3, 9],
    8:  [4, 5, 10],
    9:  [6, 7, 10],
    10: [8, 9],
}
print("BFS:", bfs(graph, 1))
print("DFS:", dfs(graph, 1))


print("\n=== Topological Sort ===")

dag = {
       7:[5,6], 
       5:[2,4], 
       6:[4,3], 
       2:[1], 
       3:[1], 
       4:[0], 
       1:[0], 
       0:[]
       }
print("Topological sort:", topological_sort(dag, [0,1,2,3,4,5,6,7]))

dag = {
    0: [3, 4],
    1: [3],
    2: [4, 5],
    3: [6],
    4: [6, 7],
    5: [7],
    6: [8],
    7: [8],
    8: [],
}
print("Topological sort:", topological_sort(dag, [0,1,2,3,4,5,6,7,8]))


print("\n=== Prim's MST ===")

graph = {
    'a': [('b',4),  ('h',8)],
    'b': [('a',4),  ('c',8),  ('h',11)],
    'c': [('b',8),  ('d',7),  ('f',2),  ('i',2)],
    'd': [('c',7),  ('e',9),  ('f',14)],
    'e': [('d',9),  ('f',10)],
    'f': [('c',2),  ('d',14), ('e',10), ('g',2)],
    'g': [('f',2),  ('h',1),  ('i',6)],
    'h': [('a',8),  ('b',11), ('g',1),  ('i',7)],
    'i': [('c',2),  ('g',6),  ('h',7)],
}
edges, weight = prims_mst(graph, 'a')
print("MST edges:", edges)
print("MST weight:", weight)

graph = {
    'A': [('B',2), ('C',3), ('D',8)],
    'B': [('A',2), ('C',1), ('E',5)],
    'C': [('A',3), ('B',1), ('D',4), ('F',6)],
    'D': [('A',8), ('C',4), ('F',2), ('G',3)],
    'E': [('B',5), ('F',7), ('H',4)],
    'F': [('C',6), ('D',2), ('E',7), ('H',1), ('I',5)],
    'G': [('D',3), ('I',2)],
    'H': [('E',4), ('F',1), ('I',3)],
    'I': [('F',5), ('G',2), ('H',3)],
}
edges, weight = prims_mst(graph, 'A')
print("MST edges:", edges)
print("MST weight:", weight)