# https://www.acmicpc.net/problem/18126
import sys
sys.setrecursionlimit(10**9)

from collections import deque

N=int(input())
graphs = [list(map(int, input().split())) for _ in range(N-1)]
Tree=[ [] for _ in range(N+1) ]
[Tree[a].append((b, c)) for a, b, c in graphs]
[Tree[b].append((a, c)) for a, b, c in graphs]

distances = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for end, distance in Tree[v]:
            if distances[end] is 0 and end is not 1:
                distances[end] = distances[v] + distance
                queue.append(end)

bfs(1)

print(max(distances))