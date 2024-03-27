#https://www.acmicpc.net/problem/2206
# 최단거리이기에 bfs를 사용

from collections import deque


def sol(nm, road):
    direc = [(-1,0),(1,0),(0,-1),(0,1)]     #방향 설정   
    n, m = nm
    que = deque([(0,0,1,1)])              # x, y, 이동, 부술수 있는 벽 수

    while que:
        x,y,move,wall = que.popleft()
        if x == n-1 and y == m-1:
            return move
        for dx,dy in direc:
            nx, ny = x +dx, y+ dy
            if 0 <= nx < n and 0 <= ny < m:
                if road[nx][ny]==0:
                    que.append((nx, ny, move + 1, wall))
                    road[nx][ny] = 2                        # 방문한 곳은 2로 표시하여 다시 방문하지 않도록 함
                    
                elif road[nx][ny] == 1 and wall > 0:
                    que.append((nx, ny, move + 1, wall -1))
                    road[nx][ny] = 2
    return -1


nm1 = [6,4]
road1 = [[0, 1, 0, 0],[1, 1, 1, 0],[1, 0, 0, 0],[0, 0, 0, 0],[0, 1, 1, 1],[0, 0, 0, 0]]

nm2 = [4,4]
road2 = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]

print(sol(nm2,road2))