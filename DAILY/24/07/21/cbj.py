# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**9)

T = int(input())

def dfs(x,y):
    if 0<=x<M and 0<=y<N and graph [y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

for i in range(T):
    # 가로, 세로, 개수
    M, N, K = map(int, input().split())
    # x가 M, y가 N
    graph = [[0]*M for _ in range(N)]
    for i in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1

    ans =0
    for i in range(M):
        for j in range(N):
            if graph[j][i] ==1:
                dfs(i, j)
                ans +=1
    print(ans)
    
