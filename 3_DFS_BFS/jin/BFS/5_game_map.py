# 1. 문제
# 0 = 벽, 1 = 길
# 동, 서, 남, 북으로 한 칸씩 이동
# 상대 진영에 도착하지 못할 땐 -1 리턴
# maps는 n x m , 2차원 배열
# n과 m은 각각 1 이상 100 이하의 자연수
# n과 m이 모두 1인 경우는 주어지지 x
# 처음 위치는 (1,1) 상대 진영 (n,m)

# 2. 고민한 답안
# BFS/1번 미로탈출 문제와 유사
# 최단경로를 찾는 점에서 BFS 선택
# 방문한 곳을 체크하고 모든 곳에 방문하지 못하면 -1 리턴

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    graph = maps


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
                # 벽인 경우 넘어감
                if graph[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if graph[nx][ny] == 1 :
                    # graph에 값을 업데이트해서 방문표시
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        # 그럼에도 방문하지 않은 노드가 있으면 -1 리턴
        return graph[n-1][m-1] if graph[n-1][m-1] > 1 else -1

    return bfs(0, 0)

