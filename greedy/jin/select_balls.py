# 1. 문제
# 볼링공 N개, 볼링공 무게는 1부터 M까지 자연수
# 서로 무게가 다른 볼링공을 고르기
# N개의 공의 무게가 각각 주어질 때, 볼링공을 고르는 경우의 수 출력

# 2. 고민한 답
# 시간 복잡도 O(n**2)

n, m = map(int, input().split())
data = list(map(int, input().split()))
count = 0

for i in range(n-1):
  for j in range(i+1,n): 
    if data[i] != data[j]:
      count += 1
 
print(count)


# 3. 효율적인 답
# 시간 복잡도 O(m+n)

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
    result = 0
    # 1부터 m까지의 각 무게에 대하여 처리

for i in range(1, m + 1):
        n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)