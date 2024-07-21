# https://www.acmicpc.net/problem/10844

# 끝자리가 중요. 0, 9로 끝나는 경우는 0은 1에서 9는 8에서 옴. 나머지는 2개씩

n = int(input())

def sol(N):
    ans = [[0] * 10 for _ in range(N)]
    ans[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # 0은 이미 입력 받았기에 1부터 시작(이는 2자리 수)
    for i in range(1,N):
        # 2부터 8까지는 -1과 +1로 부터 받음
        for j in range(1,9):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j+1]
        
        #0 과 9는 각각 1과 8에서 받아옴
        ans[i][0] = ans[i-1][1]
        ans[i][9] = ans[i-1][8]

    return sum(ans[n-1]) % 1_000_000_000

print(sol(n))