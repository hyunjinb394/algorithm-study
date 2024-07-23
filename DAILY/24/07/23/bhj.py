# 0. 문제 정보
# 1이상 10000이하의 숫자 중에서 
# 666이 들어간 수의 n번째 숫자를 찾기

# 1. 문제 풀이
from sys import stdin
input = stdin.readline

n = int(input())
jongmal = 666
count = 0

while True:
    if '666' in (str(jongmal)):
        count += 1
    if count == n :
        print(int(jongmal))
        break
    jongmal += 1


# 2. 다른 풀이

n = int(input())
jongmal = []
n = 0

while len(jongmal) < n:
    if not n%10 == 6:
        jongmal.append(n*1000+666)
    elif (n//10)%100 == 66:
        for k in range(1000):
            jongmal.append(n*1000+k)
    elif (n//10)%10 == 6:
        for j in range(100):
            jongmal.append(n*1000+600+j)
    else:
        for i in range(10):
            jongmal.append(n*1000+660+i)
    n += 1

print (jongmal[n-1])
