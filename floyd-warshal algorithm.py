
INF = 99999

n = 4

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

dist = [row[:] for row in graph]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("Shortest distance matrix:")

for row in dist:
    print(row)
