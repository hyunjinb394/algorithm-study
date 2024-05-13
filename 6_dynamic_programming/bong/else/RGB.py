# https://www.acmicpc.net/problem/1149
# 집수 N은 2이상 1,000이하
# 집 칠하는 비용 1,000이하

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# C는 cost, N은 집수(N회 반복. 좀더 정확히는 3N이 맞을듯)
def sol(C):
    ans=[0,0,0]
    re = [0,0,0]
    for i in C:             #i는 집의 페인트 cost
        ans[0] = i[0] + min(re[1],re[2])
        ans[1] = i[1] + min(re[0],re[2])
        ans[2] = i[2] + min(re[0],re[1])
        re = ans[:]         #깊은 복사 해야함
    return min(ans)
            
print(sol(cost))