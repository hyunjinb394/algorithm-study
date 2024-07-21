# https://www.acmicpc.net/problem/1303

# W가 우리팀, B가 상대
import sys
sys.setrecursionlimit(10**9)

N, M = map(int,input().split())
warriers = [list(input()) for _ in range(M)]


def dfs(who,x,y):
    global point
    if 0<=x<N and 0<=y<M and warriers[y][x] == who:
        warriers[y][x] = 0
        point += 1
        dfs(who,x+1,y)
        dfs(who,x-1,y)
        dfs(who,x,y+1)
        dfs(who,x,y-1)

me_sum=0
oppo_sum=0

for i in range(N):
    for j in range(M):
        point =0
        if warriers[j][i] != 0:
            dfs('W',i,j)
            me_sum += point **2
        if warriers[j][i] != 0:
            dfs('B',i,j)
            oppo_sum += point **2
print(me_sum,oppo_sum)