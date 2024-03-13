# 1. 문제
# N개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값

# 2. 고민한 답
# 금액을 1부터 오름차순으로 만들 수 있는지 확인
# 금액보다 단위가 작을 경우 금액을 만들 수 있음
# 금액을 만들 수 있으면 값을 갱신
# 금액보다 더 큰 값이 단위로 주어지면 해당 수는 답으로 출력

n = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1
for x in data :
    if target < x :
        break
    target += x

print(target)
