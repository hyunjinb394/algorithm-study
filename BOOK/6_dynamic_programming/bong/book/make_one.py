#시간 제한 1초, 메모리 제한 128mb

def one_make(X):
    # 숫자별 리스트 생성
    dp = [0] * (X + 1)

    # x는 1인경우 0, 2인경우 부터 1이상이므로 2부터 시작
    for i in range(2, X + 1):

        #첫번째 가정은 이전 숫자 +1 회가 가장 작은 경우 
        dp[i] = dp[i-1] + 1

        #자신의 숫자의 /2한 숫자가 존재하며 그 횟수가 자기 바로 이전 숫자 횟수 보다 작은 경우 이를 채택. 이후는 동일
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5] + 1)


    return dp[X]

X = int(input())
print(one_make(X))

        