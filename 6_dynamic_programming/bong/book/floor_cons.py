# 가로줄 N(1<N<1,000)

n = int(input())

def count(N):
    ans = [0]*N
    ans[0] = 1
    ans[1] = 3

    for i in range(3,N):
        # [i-1]의 경우 우측 짝대기 하나 추가한다는 경우, [i-2]의 경우 세로 짝대기 2개는 이미 [i-1]에서 카운트, 가로 짝대기 2개, 큰거 한개의 경우  
        ans[i] =(ans[i-1]+2*ans[i-2]) % 796796
    
    print(ans[N-1])

