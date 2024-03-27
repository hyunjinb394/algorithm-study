# 1. 문제
# 백준 2606번 / BFS & DFS / 네트워크 유형 
# 연결되어 있는 네트워크끼리는 웜 바이러스가 걸림
# 1번 컴퓨터가 바이러스에 감염될때, 감염되는 컴퓨터의 수 출력
# 첫 줄 : 컴퓨터 수 100이하 양의 정수
# 둘째 줄 : 네트워크상 직접 연결된 컴퓨터 쌍의 수
# 이어서 한 줄에 한 쌍씩 네트워크 상 연결된 컴퓨터 번호 쌍 주어짐

# 2. 고민한 답안

# 스택을 사용한 답안

# 컴퓨터의 개수
N = int(input()) 
# graph[n]에는 n번 컴퓨터와 연결된 컴퓨터들을 저장
graph = [[] for _ in range(N+1)]

# 그래프에 컴퓨터들 간의 연결 관계 저장
for _ in range(int(input())): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 체크 여부 저장할 배열
checked = [False] * (N+1)
checked[1] = True

# 1번 컴퓨터에서 바이러스 시작
stack = [1]

# DFS
while stack: # 더 이상 확인할 컴퓨터가 없으면 break
    curr = stack.pop() # 최근에 감염된 컴퓨터부터 확인

    for next in graph[curr]: # curr 번 컴퓨터와 연결된 컴퓨터들 순회
        if not checked[next]: # 아직 체크 안한 컴퓨터라면
            checked[next] = True # 체크
            stack.append(next) # 이 컴퓨터랑 연결된 컴퓨터도 체크

print(checked.count(True)-1) # 1번 컴퓨터 빼고 감염된 컴퓨터의 수 출력


# 재귀함수를 사용한 풀이
N = int(input()) # 컴퓨터 개수
graph = [[] for _ in range(N+1)] # 그래프 초기화

for _ in range(int(input())) : 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, count):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            count = dfs(node, count+1)
    return count

visited = [False for _ in range(int(input())+1)]
print(dfs(1, 0))

