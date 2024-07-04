# 0. 문제 정보
# 백준 18126번 / 그래프 탐색
# https://www.acmicpc.net/problem/18126
# 시간제한 1초, 메모리제한 1024 MB

# 1. 문제 이해
# 입구는 한개, n개의 방, n-1개의 길
# 길에 대한 정보가 A,B,C로 주어짐
# A과 B번 방 사이를 양방향으로 연결하는 길의 길이가 C임
# 입구와 가장 먼 방에 아이스크림을 숨김

# 2. 문제 풀이(dfs) / 56ms , 33969 KB
import sys
# 재귀 호출 깊이 정하기
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())

def dfs(now):
    visited[now] = 1
    for i in range(len(adj_list[now])):
        # 연결된 노드 n
        n = adj_list[now][i][0]
        # 방문하지 않은 노드
        if not visited[n]:
            # n과 현재 노드 사이의 거리 더하기
            distance[n] = adj_list[now][i][1] + distance[now]
            dfs(n)


visited = [0 for i in range(N+1)]
adj_list = [[] for i in range(N+1)]

# 각 노드까지 거리
distance = [0 for i in range(N+1)]

# 입력받기
for i in range(1, N):
    a, b, c = map(int, sys.stdin.readline().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

# 1번이 입구
dfs(1)
print(max(distance))



# 3. bfs로 풀기 / 60ms, 34060 KB
from collections import deque

def bfs(now, n, graph):
    queue = deque([now])
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    visited[now] = True
    max_distance = 0

    while queue:
        node = queue.popleft()
        for next_node, dist in graph[node]:
            # 방문하지 않았으면
            if not visited[next_node]:
                # 방문 표시 + 거리 더하기
                visited[next_node] = True
                distance[next_node] = distance[node] + dist
                queue.append(next_node)
                # bfs라 모든 경로의 거리를 비교해야함
                if distance[next_node] > max_distance:
                    max_distance = distance[next_node]
    
    return max_distance

def main():
    n = int(input().strip())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        a, b, c = map(int, input().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    result = bfs(1, n, graph)
    print(result)

if __name__ == "__main__":
    main()



# 봉준님 풀이
# DFS
import sys
sys.setrecursionlimit(10*9)

N=int(input())
graphs = [list(map(int, input().split())) for _ in range(N-1)]
Tree=[ [] for _ in range(N+1) ]

[Tree[a].append((b, c)) for a, b, c in graphs]
[Tree[b].append((a, c)) for a, b, c in graphs]

distances = [0] (N+1)

# graph: (목적지, 거리), v:시작점
def dfs(graph, v):
        for end, distance in graph[v]:
            if distances[end] is 0  and end is not 1:
                distances[end] = distances[v] + distance
                dfs(graph, end)

dfs(Tree,1)
print(max(distances))

# BFS
import sys
sys.setrecursionlimit(10*9)

from collections import deque

N=int(input())
graphs = [list(map(int, input().split())) for _ in range(N-1)]
Tree=[ [] for _ in range(N+1) ]
[Tree[a].append((b, c)) for a, b, c in graphs]
[Tree[b].append((a, c)) for a, b, c in graphs]

distances = [0] (N+1)

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