# https://www.acmicpc.net/problem/12865
# 물품수 N은 1에서 100사이
# 버틸수 있는 무게 K는 1에서 100,0000사이. 
# 각 물건의 무게 W는 1에서 100,000사이.
# 물건의 가치 V는 0에서 1,000사이

#인터넷 풀이임
def knapsack(N, K, weights, values):
    # K는 각각 버틸 수 무게, N은 
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # 각 물건을 하나씩 고려하며 DP 테이블 채우기
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            # 현재 물건을 가방에 넣을 수 없는 경우
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            # 현재 가능 무게에서 이전것과 
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
        print(dp[i])
    
    # 최대 가치 반환
    return dp[N][K]

# 입력 받기
N, K = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 결과 출력
print(knapsack(N, K, weights, values))
