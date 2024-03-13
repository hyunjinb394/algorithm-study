# 1. 문제
# N이 1이 될때까지 1을 빼거나 K로 나누고 수행 과정의 최솟값 출력
# 빼는 것보다 나누는 것이 값이 더 많이 줄어듦
# 최대한 많이 나눠야함


#2. 고민한 답
n,k = map(int, input().split())
count = 0

while n != 1:
    if n % k != 0 :
       n -=1
       count += 1
    else :
        n //= k
        count += 1

print(count) 


#3. 효율적인 답


n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)