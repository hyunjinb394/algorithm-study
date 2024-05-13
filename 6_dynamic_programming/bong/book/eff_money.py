# N개의 화폐(1<=N<=100)
# M원 을 만들수 있는 가장 작은 화폐 수

n, m = map(int,input().split())
mlist = [int(input()) for _ in range(n)]

def check(mlist, N, M):
    ans = [10_000]*10_000
    ans[0] = 0
    for i in range(N):
        for j in mlist:
            if ans[i]
