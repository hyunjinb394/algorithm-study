# #https://www.acmicpc.net/problem/2206
# # 최단거리이기에 bfs를 사용

# from collections import deque


# def sol(n,m, road):
#     direc = [(-1,0),(1,0),(0,-1),(0,1)]     #방향 설정   
#     que = deque([(0,0,1,1)])              # x, y, 이동, 부술수 있는 벽 수

#     while que:
#         x,y,move,wall = que.popleft()
#         if x == n-1 and y == m-1:
#             return move
#         for dx,dy in direc:
#             nx, ny = x +dx, y+ dy
#             if 0 <= nx < n and 0 <= ny < m:
#                 if road[nx][ny]==0:
#                     que.append((nx, ny, move + 1, wall))
#                     road[nx][ny] = 2                        # 방문한 곳은 2로 표시하여 다시 방문하지 않도록 함
                    
#                 elif road[nx][ny] == 1 and wall > 0:
#                     que.append((nx, ny, move + 1, wall -1))
#                     road[nx][ny] = 2
#     return -1


# n,m = 5,4
# road1 = [[0, 1, 0, 0],
#          [1, 1, 1, 0],
#          [0, 0, 0, 0],
#          [0, 1, 1, 1],
#          [0, 0, 0, 0]]

# # n,m = 4,4
# road2 = [
#     [0, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 0]]

# print(sol(n,m,road1))

from collections import deque

n, m = map(int, input().split())
road = [list(map(int, input())) for _ in range(n)]


direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
que = deque([(0, 0, 1, 1)])  # x, y, 이동, 부술수 있는 벽 수

while que:
    x, y, move, wall = que.popleft()
    if x == n - 1 and y == m - 1:
        print(move)
        exit(0)
    for dx, dy in direc:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if road[nx][ny] == 0 :
                que.append((nx, ny, move + 1, wall))
                road[nx][ny] = 2  # 방문한 곳은 2로 표시하여 다시 방문하지 않도록 함
            elif road[nx][ny] == 1 and wall == 1:  # 벽을 부수고 이동하는 경우
                que.append((nx, ny, move + 1, wall - 1))
                road[nx][ny] = 2
print(road)
print(-1)



'''예외케이스
$ python b_break_wall.py
6 7
0111111
0110000
0110110
0110110
0010111
-1
'''

