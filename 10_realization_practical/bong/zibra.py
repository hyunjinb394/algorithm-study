#https://www.acmicpc.net/problem/30454

N, L = map(int,input().split())
hairs = [list(map(int,input())) for _ in range(N)]

def strip(lines):
    strips = 0
    now = 0
    for i in range(len(lines)):
        if now == 0 and lines[i]==1:
            now = 1
            strips +=1
        elif now ==1 and lines[i] ==0:
            now = 0
    return strips


ans = 0
ans_num = 0
for hair in hairs:
    now_hair = strip(hair)
    if ans < now_hair:
        ans_num = 0
    ans = max(ans,now_hair)
    if ans == now_hair:
        ans_num += 1
print(ans, ans_num)