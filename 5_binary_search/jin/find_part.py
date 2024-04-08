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