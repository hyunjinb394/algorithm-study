# 0. 문제 이해
# 연속된 수를 선택해 가장 큰 합을 만들기
# 한 개 이상 선택

# 입력
# n : 정수 개수, 10^5
# n 개의 정수로 이루어진 수열
# 수열의 수는 -1000 이상 1000 이하의 정수

# 출력
# 첫 줄에 답 출력

# 1. 문제 풀이
# 처음엔 리스트의 max값을 찾아서 좌우로 더해나가는 로직으로 구성
# 다른 연속된 수들의 합이 max 값보다 큰 case를 해결하지 못함

# 전체 리스트를 하나씩 돌면서 더하면서 비교해야함
# DP / 카데인 알고리즘

from sys import stdin
input = stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

# 리스트를 돌면서
for i in range(1, n):
# 현재 값과 이전의 합을 더한 값의 max값을 찾기
# 모든 케이스가 다 적용됨
    num_list[i] = max(num_list[i], num_list[i-1]+ num_list[i])

print(max(num_list))
