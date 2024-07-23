# 0. 그래프 이론 / 연결된 곳 체크하기 

# 1. 문제풀이
# 방문한 배추는 1 -> 0 으로 처리
# 2차원 배열로 배추 위치 기록

# sys에서 사용할 객체만 임포트 하기 
from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def cabbage_group(x,y):
    # 방문한 배추는 0으로 바꾸기
    field[x][y] = 0
    # 인접한 배추들 모두 dfs로 확인하기 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == 1:
            cabbage_group(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]* n for _ in range(m)]

    for _ in range(k):
        x,y = map(int, input().split())
        field[x][y] =1

    count = 0

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                # 전체 2차원 배열을 돌면서 dfs 실행된 횟수를
                # count로 증가시키기
                cabbage_group(i, j)
                count += 1
    
    print(count)



