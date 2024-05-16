# 1. 문제 이해
# 각 줄에 드어간 케이스를 2,3의 합으로 나타나는 경우의 수
# 1로만 나타내는 경우의 수는 1개

# 2. 문제 풀이
# 1,2,3으로 더해지는 수가 연속될 수 없음
# n이라는 숫자를 만들기 위한 경우의 수는 n-i를 만들기 위한 경우의 수 + 3

c = 1000000009

# n 숫자개수 numbers 입력받은 숫자 리스트
def countAdd(n, numbers):
    max_num = max(numbers)
    
    # dp 배열 초기화
    # 마지막 숫자가 1, 2, 3 인 경우
    dp1, dp2, dp3 = [0] * (max_num + 1), [0] * (max_num + 1), [0] * (max_num + 1)
    
    if max_num >= 1:
        dp1[1] = 1
    if max_num >= 2:
        dp2[2] = 1
    if max_num >= 3:
        # 마지막 숫자가 1,2,3일때 3을 만들 수 있는 경우의 수
        dp1[3] = dp2[3] = dp3[3] = 1
    
    # 점화식
    for i in range(4, max_num + 1):
        dp1[i] = (dp2[i-1] + dp3[i-1]) % c
        dp2[i] = (dp1[i-2] + dp3[i-2]) % c
        dp3[i] = (dp1[i-3] + dp2[i-3]) % c

    results = []
    for num in numbers:
        result = (dp1[num] + dp2[num] + dp3[num]) % c
        results.append(result)
    
    return results

import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
numbers = [int(data[i]) for i in range(1, n + 1)]


results = countAdd(n, numbers)
for result in results:
    print(result)