n = 8
A = [[0,1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

adj = []
for i in range(n):
    adj.append([0] * n)

for r in range(len(adj)):
    print(f"{r}: {adj[r]}")

print("-----------Directional----------------------")

for u, v in A:
    adj[u][v] = 1
    

for r in range(len(adj)):
    print(f"{r}: {adj[r]}")

print("-----------Undirectional----------------------")

for u, v in A:
    adj[u][v] = 1
    adj[v][u] = 1

for r in range(len(adj)):
    print(f"{r}: {adj[r]}")
