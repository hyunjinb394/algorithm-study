# N개의 화폐(1<=N<=100)
# M원 을 만들수 있는 가장 작은 화폐 수(1<=M<=10,000)

n, m = map(int,input().split())
mlist = [int(input()) for _ in range(n)]

#n*m회 계산. 최대 10^6회이므로 최대 약 0.1초.
def sol(mlist, M):
    # 10,001개인 이유는 0부터 10,000까지의 수를 확인해야 하기 때문(근데 0은 경우에 없음)
    ans = [0]*10_001

    #M원 까지 확인을 위해 M+1(i는 화폐)
    for i in range(M+1): #(j는 리스트에 있는 수)
        for j in mlist:
            if i == j: ans[i] = 1       # 최소 단위일 시 1

            # 현재 숫자 - 최소 단위 존재시 거기에 +1(어짜피 가장 큰수를 마지막으로 확인하기에 가장 적은 숫자를 활용하는 경우가 사용됨)
            if ans[i-j] != 0:                           ans[i]=ans[i-j]+1

    if ans[M] == 0: return -1

    return ans[M]

print(sol(mlist,m))
