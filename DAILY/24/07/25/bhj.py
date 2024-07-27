# 0. 문제 이해
# 막걸리 주전자 안에 막걸리 용량이 랜덤
# k명에게 모든 막걸리를 동일하게 분배 후 막걸리가 남으면 버림
# ex. 1002, 802, 705ml의 3개의 막걸리가 있다면 401ml로 동등하게 나누기
# 각각의 주전자의 용량을 k로 나눴을때 최대 용량을 구하는 것

# 입력
# n : 주전자 수 , k : 사람 수
# 주전자 용량이 n개 만큼 입력
# n은 10^4 이하 정수 k는 10^6이하 정수
# 시간복잡도를 낮추는 풀이를 선택해야함
# 막걸리 용량은 2^31-1보다 작거나 같은 정수 
# 단 n <= k

# 출력
# k명에게 나눠줄 수 있는 최대한의 막걸리 용량 ml로 

# 1. 문제 풀이

from sys import stdin

input= stdin.readline

n, k = map(int, input().split())
drinks = [int(input()) for _ in range(n)]

# 이분탐색(logN)으로 풀어야할거 같은데 어떻게 풀더라..?
# 중앙값 찾고 값이 크면 start를 키우고 값이 작으면 right를 줄이기

start, end = 1, max(drinks)

while start <= end :
    mid = (start + end ) // 2
    tmp = 0

    for drink in drinks:
        tmp += drink // mid

    if tmp >= k:
        start = mid + 1
        
    else: 
        end = mid - 1



print(end) 






# 2. 다른 풀이 


from sys import stdin

input= stdin.readline

n, k = map(int, input().split())
drinks = [int(input()) for _ in range(n)]

start, end = 1, max(drinks)


while start <= end :
    mid = (start + end ) // 2

# 이 부분을 리스트컴프리핸션으로 작성하면 20% 정도 빨라짐
    tmp = sum(i // mid for i in drinks)


    if tmp >= k:
        start = mid + 1
        
    else: 
        end = mid - 1



print(end) 

