# 1. 문제


# 2. 고민한 답안

n = int(input()) # 전체 부품 수
store_parts = set(map(int, input.split())) # 전체 부품 번호

order_num = int(input()) # 주문한 부품 수
order_parts = list(map(int, input().split())) # 주문한 부품 번호

for i in order_parts :
    if i in store_parts :
        print('yes', end= ' ')
    else:
        print('no', end=' ')

# 3. 이진 탐색 챕터니까 이진탐색으로 풀어보자

def binary_search(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else :  
            start = mid + 1
        return None
    
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    m = int(input())
    x = list(map(int,input().split()))

    for i in x :
        result = binary_search(array, i, 0, n-1)
        if result != None:
            print('yes', end=' ')
        else : 
            print('no', end=' ')


# 4. 팀원 풀이


# 혁준
# 각 부품이 존재하면 yes, 없으면 no 공백으로 구분
def solution(N,n_list, M,m_list):
    def Bsearch(start, end, target, array):
        if start > end:
            return None
        
        mid = (start+end)//2
        if array[mid] > target:
            return Bsearch(start, mid-1, target, array)
        if array[mid] < target:
            return Bsearch(mid+1, end, target, array)
        if array[mid] == target:
            return mid
    
    n_list.sort()

    for m in m_list:
        result = Bsearch(0, N-1, m, n_list)
        if result is not None:
            print('yes', end=' ')
        else:
            print('no', end=' ')



# 봉준
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

