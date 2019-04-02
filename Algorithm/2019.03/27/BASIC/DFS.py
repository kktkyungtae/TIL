from collections import deque

def DFS(u):  # s:시작점 # 방문 정점 u로 변경
    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            P[v] = u
            DFS(v)


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, W = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u,w))


D = [0xffff] * (V + 1)
P = [i for i in range(V + 1)]
D[s] = 0
DFS(1)