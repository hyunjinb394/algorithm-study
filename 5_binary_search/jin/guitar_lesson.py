# 1. 문제
# 강의 수 : N (1 ≤ N ≤ 100,000)
# 블루레이 수 : M (1 ≤ M ≤ N) 
# 강의 길이 ≤ 10000
# 강의는 연속해서 녹화해야함
# 전체 강의를 블루레이에 나눠서 녹화, 블루레이 크기는 모두 동일
# 블루레이의 최소 크기 출력

# 2. 고민한 답안

n, m = map(int, input().split())
lesson = list(map(int,input().split()))

start = max(lesson)
end = sum(lesson)

while start <= end:
    
    mid = (start + end) // 2 #블루레이 크기

    total, count = 0 ,1  #블루레이 길이,블루레이 개수

    for i in lesson:
        if total + i > mid: #블루레이 길이가 mid 보다 크면
            count += 1 #블루레이 개수 +1
            total = 0 
        total += i 

    if count <= m: #블루레이 개수가 적으면
        ans = mid
        end = mid - 1 #블루레이 크기를 줄이기
    else: #블루레이 개수가 많으면
        start = mid + 1 #블루레이 크기를 늘리기
    
print(ans)


