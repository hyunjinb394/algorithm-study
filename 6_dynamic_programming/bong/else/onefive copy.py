import sys
input = sys.stdin.readline

n = int(input())

def sol(L):   #L은 가장 큰수
    ans = [[1,0,0],[0,1,0],[1,1,1]]

    if L <= 3: return ans

    for i in range(3,L):       
        ans.append([ans[i-1][1] + ans[i-1][2], ans[i-2][0] + ans[i-2][2], ans[i-3][0] + ans[i-3][1]])

    return ans

ans = sol(100001)


for i in range(n):
    print(sum(ans[int(input())-1])% 1_000_000_009)