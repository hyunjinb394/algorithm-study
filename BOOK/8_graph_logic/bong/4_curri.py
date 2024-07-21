n = int(input())
datas = [list(map(int, input().split())) for _ in range (n)]

# 개별 시간 list
time = [0]+[i[0] for i in datas]

# 선행 list
pre = [0]+[i[1:-1] for i in datas]


for i in range(1,n+1):
    if len(pre[i]) == 0:
        print(time[i])
