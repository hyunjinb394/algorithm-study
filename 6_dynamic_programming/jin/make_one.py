# 1. 문제 이해
# 연산 4개
# 5,3,2로 나눔 || 1을 뺌
# x 주어졌을때 x를 1로 만들기 위한 최소 연산 횟수

# 2. 문제 풀이 (Bottom Up)
# 38.932 MB / 540 ms 
# 계산된 상태를 반복적으로 사용하는 것

import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
       dp[i] = min(dp[i], dp[i//2] + 1) 
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0 :
        dp[i] = min(dp[i], dp[i//5] + 1)
print(dp[n])


# 3. Top down으로 재귀적으로 풀어본다면?

import sys
# 재귀 호출의 리밋을 설정하기
# 백준에서 메모리 초과
sys.setrecursionlimit(30000)

def make_one(n, dp):
    if n == 1:
        return 0
    if dp[n] != -1:
        return dp[n]

    dp[n] = make_one(n - 1, dp) + 1

    if n % 2 == 0:
        dp[n] = min(dp[n], make_one(n // 2, dp) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], make_one(n // 3, dp) + 1)
    if n % 5 == 0:
        dp[n] = min(dp[n], make_one(n // 5, dp) + 1)
    
    return dp[n]

n = int(sys.stdin.readline())
dp = [-1] * (n + 1)
print(make_one(n, dp))