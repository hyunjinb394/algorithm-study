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



# 4. 팀원 풀이

# 혁준
from collections import deque

def solution(N,M,mat):
    sol = BFS(N,M,mat)
    print(sol)

def BFS(N,M,mat):
    que = deque()
    que.append((0,0))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while que:
        n, m = que.popleft()

        for i in range(4):
            x = m+dx[i]
            y = n+dy[i]
            if x<0 or x>=M or y<0 or y>=N:
                continue
            else:
                if mat[y][x] == 1:
                    que.append((y,x))
                    # 미로의 경로 자체에 몇 칸 지났는지 기록
                    mat[y][x] = mat[n][m] + 1
    return mat[N-1][M-1]


# 봉준

def sol(road):
    n = len(road)                            #지도의 가로 길이
    m = len(road[0])                         #지도의 세로 길이
    direc = [(-1,0),(1,0),(0,-1),(0,1)]     #방향 설정    

    que = deque([(0,0,1)])                  #위치 + 지나간 거리
    
    while que:
        x,y,move = que.popleft()
        if x == n - 1 and y == m - 1:  # 상대 팀 진영 도착 시 거리 반환
            return move

        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 1:
                que.append((nx, ny, move + 1))
                road[nx][ny] = 0  # 방문한 곳은 0으로 표시하여 다시 방문하지 않도록 함

    return -1  # 상대 팀 진영에 도착할 수 없는 경우