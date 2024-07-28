# https://www.acmicpc.net/problem/13702

# N주전자 수, K는 인원수
N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]

#이진 탐색 사용
start = 1
end = max(X)

result = 0

while start <= end:
    total = 0
    mid = (start + end)//2

    # i//mid는 주전자 하나당 몇 명 먹을 수 있는지
    for i in X:
        total += i//mid

    if total>=K:
        result = mid
        start = mid+1
    else:
        end=mid-1
print(result)