# 0. 문제 정보
# 백준 1261번 / 그래프 탐색
# https://www.acmicpc.net/problem/1261
# 시간제한 1초, 메모리제한 128 MB

# 1. 문제 이해
# N * M 크기
# 상하좌우 인접한 방만 벽을 부수면서 이동 가능
# (1,1)에서 (N,M)으로 이동하기 위해 부숴야하는 최소 한의 벽의 개수 출력


# 2. 문제 풀이(시간 72ms / 메모리 34192 KB)
# 전형적인 0-1 BFS 알고리즘 사용해야하는 문제
# 간선의 가중치가 0이면 앞에, 1이면 뒤에 넣는 방식

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

M,N = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

q = deque()
q.append((0,0))
visited[0][0] = 0

while q: 
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
            if matrix[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx,ny))
            else:
                visited[nx][ny] = visited[x][y] +1
                q.append((nx,ny))

print(visited[N-1][M-1])
