import math


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, src, end):

        dist = [math.inf] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != math.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        matrix = [[math.inf for j in range(len(dist))] for i in range(len(dist))]
        for i in self.graph:
            matrix[i[0]][i[1]] = i[2] + dist[i[0]] - dist[i[1]] # новое значение получаем по формуле Форда-Беллмана

        # for i in matrix:
        #     print(i)

        def arg_min(T, S):
            amin = -1
            m = math.inf
            for i, t in enumerate(T):
                if t < m and i not in S:
                    m = t
                    amin = i

            return amin

        N = len(matrix)
        T = [math.inf] * N

        v = 0
        S = {v}
        T[v] = 0
        M = [0] * N

        while v != -1:
            for j, dw in enumerate(matrix[v]):
                if j not in S:
                    w = T[v] + dw
                    if w < T[j]:
                        T[j] = w
                        M[j] = v

            v = arg_min(T, S)
            if v >= 0:
                S.add(v)


        path = [end]
        while end != src:
            end = M[path[0]]
            path = [end] + path

        return path

def jon(size, tuples, start, end):
    g = Graph(size)
    for i in tuples:
        g.addEdge(i[0], i[1], i[2])

    return g.BellmanFord(start, end)
# g = Graph(4)
# g.addEdge(0, 1, -7)
# g.addEdge(0, 2, -3)
# g.addEdge(1, 2, 2)
# g.addEdge(1, 3, 3)
# g.addEdge(2, 3, -4)

# Print the solution
# print(jon(4, [(0, 1, -7), (0, 2, -3), (1, 2, 2), (1, 3, 3), (2, 3, -4)], 0, 3))
# print(g.BellmanFord(0, 3))