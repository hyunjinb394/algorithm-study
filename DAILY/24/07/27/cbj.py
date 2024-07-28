# https://www.acmicpc.net/problem/1912

N = int(input())
NLIST = list(map(int,input().split()))

ans = 0
pre_ans=0

if max(NLIST)<0:
    ans = max(NLIST)
else:
    for i in range(N):
        ans += NLIST[i]
        pre_ans = max(ans,pre_ans)
        if ans < 0:
            ans = 0
    if pre_ans > ans:
        ans = pre_ans
print(ans)