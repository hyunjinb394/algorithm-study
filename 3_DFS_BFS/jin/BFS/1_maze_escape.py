# 1. 문제
# n * m 미로 탈출, 현재 위치 (1,1)
# 출구는 (n,m) , 한 번에 한 칸씩
# 괴물 유 : 0, 무 : 1
# 탈출하기 위한 최소 칸 개수 출력
# 시작, 마지막 칸 포함해서 계산
# N, M(4 ≤ N, M ≤ 200) 
# 시작 칸과 마지막 칸은 항상 1이다.

# 2. 고민한 답안
# 특정 지점에서 연결된 노드를 다 하나씩 탐색 후 저장
# 모든 경로를 한칸씩 탐색해야하므로 BFS가 효율적
# 방문한 곳과 이동칸을 나눠서 체크

from collections import deque


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방문 기록
check = [[0]*m for _ in range(n)]

# 이동칸 기록
count = [[0]*m for _ in range(n)]

# 이동방향
dx = [-1, 1 ,0 ,0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        # 현재 위치를 큐에서 꺼낸 위치로 갱신
        x,y = queue.popleft()

        for i in range(4):
            # 인접 노드 위치
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내 있는지
            if nx >=0 and nx < n and ny >= 0 and ny < m:
                # 방문하지 않았고 & 괴물이 없는 곳
                if (check[nx][ny] == 0 and graph[nx][ny] == 1) :
                    queue.append((nx,ny))
                    # nx, ny 방문 표시
                    check[nx][ny] =1 
                    # 이동 횟수 추가
                    count[nx][ny] = count[x][y] + 1

    return count[n-1][m-1]

print(bfs())

# 3. 효율적인 답안 (책 풀이)

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# 이동방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()  # 현재 위치

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어난 경우 넘어감
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물 있는 곳일 경우 넘어감
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1 :
                # graph에 값을 업데이트해서 방문표시
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))
