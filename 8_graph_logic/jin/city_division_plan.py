# 1. 문제 이해
# 자유를 찾아 떠난 원숭이 한 마리 🐒
# 평화로운 마을에 도착
# 도로공사 문제
# n개의 집과 m개의 길, 길은 유지비가 든다
# 마을을 2개로 분할하려고 함
# 분할된 각 마을의 집들 사이에는 집을 잇는 길이 존재해야함
# 길을 없애고 유지비를 줄이고 싶음
# 유지비가 최소가 되도록 그래프로 쪼개 보아라


# 2. 문제 풀이 (시간 초과)
# 최소 신장 트리 알고리즘으로 구하기
# 그리고 유지비가 제일 비싼 길을 끊어버리면 되지 않나

# 루트 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 값들 입력받기
N, M = map(int, input().split())
edges = []
parent = [i for i in range(N + 1)]  
total_cost = 0

# 간선 리스트 정렬
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

# 크루스칼 알고리즘으로 최소 신장 트리 만들기
for edge in edges:
    cost, A, B = edge
    root_A = find(parent, A)
    root_B = find(parent, B)

    if root_A != root_B:
        parent[root_B] = root_A
        total_cost += cost

# 간선 확인해서 가장 비싼 간선 cost 제거

max_cost = max([edge[0] for edge in edges if find(parent, edge[1]) != find(parent, edge[2])])

total_cost -= max_cost

print(total_cost)



# 3. 더 효율적인 방법이 있나보다

# 입력받을 때 sys 사용 안하면 시간초과 뜸 
import sys
input = sys.stdin.readline

# 루트 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 값들 입력받기
N, M = map(int, input().split())
edges = []
parent = [i for i in range(N + 1)]
total_cost = 0
max_edge_cost = 0  # 가장 비싼 간선의 비용 저장 변수

# 간선 리스트 정렬
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

# 크루스칼 알고리즘으로 최소 신장 트리 만들기
for edge in edges:
    cost, A, B = edge
    root_A = find(parent, A)
    root_B = find(parent, B)

    if root_A != root_B:
        parent[root_B] = root_A
        total_cost += cost
        max_edge_cost = max(max_edge_cost, cost)  

# 결과 출력
print(total_cost - max_edge_cost)