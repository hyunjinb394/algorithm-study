# 1. 문제
# n * m 행렬 맵
# 이동 가능 - 0, 벽 - 1
# (1,1)에서 (n,m)까지 최단 경로로 이동
# 시작과 끝도 포함
# 벽 1개를 부수고 이동했을 때 경로가 더 짧으면 단 1개만 부수기 가능
# 최단 경로 이동 불가능하면 -1 리턴

# 2. 고민한 답안
# 미로 탈출과 비슷하지만, 벽을 부시고 가는걸 체크해야함
# 체크되면 벽은 더이상 탐색 경로가 아님

from collections import deque

n,m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
graph = [list(map(int, input())) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 범위를 넘어가면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))

