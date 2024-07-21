# 첫줄 (2 <= N <= 1,000), (1 <= M <= 10,000), (1 <= K <= 10,000) 중 하나 주어짐.
# 둘째 줄 N개의 숫자, 각 숫자는 1이상 10,000이하
# 둘째 줄에 있는 숫자 사용, M번 더함, K회 반복 가능, K는 M보다 작거나 같음

N = int(input('N을 입력 하시오(2이상, 1,000이하) : '))
M = int(input('M을 입력하시오(1이상, 10,000이하) : '))
K = int(input('K를 입력하시오(1이상, M 이하) : '))

data = list(map(int, input().split()))
data.sort()

a,b = data[N-1],data[N-2]

aa = M//(K+1)

if M%(K+1)==0:
    ba = aa
else:
    ba = aa-1

answ = a*aa*K + b*ba

print(answ)