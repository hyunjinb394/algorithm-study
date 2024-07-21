# 1. 문제 이해
# 도시의 개수 N, 통로의 개수 M, 시작 도시 C를 입력
# M개의 통로 정보를 입력
# 시작 도시 C에서 출발하여 각 도시로 가는 최단 거리를 계산


# 2. 문제 풀이

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())


graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)


for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 갱신된 거리를 큐에 추가
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)


count = 0
max_distance = 0

for d in distance:
    # distance 순회하면서 inf 가 아닌 값을 찾아
    if d != INF:
        # 도달 가능한 도시의 개수와 먼 도시까지 거리를 계산..
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1을 출력
print(count - 1, max_distance)
