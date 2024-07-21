#혁준 게임맵 최단과 완벽히 동일

from collections import deque

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

a =[[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
print(sol(a))