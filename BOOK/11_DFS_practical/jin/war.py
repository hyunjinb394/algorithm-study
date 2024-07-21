# 1. 문제 이해
# 아군 흰색, 적군 파란색
# 같은 팀 병사가 모이면 강해짐
# n명이 뭉치면 n^2 위력

# 2. 문제 풀이
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, soldiers, color):
  # 현재 지점 방문 0으로 표시
  graph[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 그래프 범위 내 있고
    if(0 <= nx < m and 0 <= ny < n):
      # 방문한적이 없으면 현재 지점에서 dfs 호출
      if(graph[nx][ny] == color):
        soldiers = dfs(nx, ny, soldiers + 1, color)
  return soldiers

n, m = map(int, input().split()) 
graph = [list(input()) for _ in range(m)]

# 방향 정하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

white_power = 0
blue_power = 0

for i in range(m):
  for j in range(n):
# 각 노드의 인접한 병사들의 n^2을 출력
    if(graph[i][j] == 'W'):
      white_power += (dfs(i, j, 1, 'W'))**2
    elif(graph[i][j] == 'B'):
      blue_power += (dfs(i, j, 1, 'B'))**2

print(white_power, blue_power)


