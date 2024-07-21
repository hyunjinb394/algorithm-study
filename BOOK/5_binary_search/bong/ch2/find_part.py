# 10^6개의 부품 가능, 번호 역시 10^6개. 찾는 부품은 10^5개이하.
# 시간 제한 1초, 메모리 128mb. 2NlogN이라면 힘들 수도 있음.

# n = int(input('부품수 : '))
# nlist = [int(input()) for _ in range(n)]

# m = int(input('찾을 부품수 : '))
# mlist = [int(input()) for _ in range(m)]

import random
import time
random.seed(1)

n = 1000000
nlist = random.sample(range(1,n+1),n)

m = 100000
mlist = random.sample(range(1,1+n),m)

now = time.time()

check = [0]*n

for i in nlist:
    check[i-1] = 1                  #시간복잡도 n회

for j in mlist:                     #t시간복잡도 m회
    if check[j-1] == 1:
        print('yes',end = ' ')
    else: print('no', end = ' ')

end = time.time()
print(end-now)

