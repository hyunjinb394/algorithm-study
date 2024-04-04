# 1. 문제
# 컴퓨터 개수 n
# computers : 2차원 배열, 컴퓨터 연결 정보 
# 네트워크 개수 return 
# n은 1 이상 200 이하
# 연결은 computers[i][j] = 1로 표현


# 2. 고민한 답안 (시간 0.5 ms/ 메모리 0.00390625 MB)
import time
import psutil
import os

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024) 

start_time = time.time()
start_memory = memory_usage()

# def solution(n, computers):            
#     answer = 0
#     visited = [0 for i in range(len(computers))]

#     def dfs(i):
#         visited[i] = 1
#         for a in range(n):
#             # i가 방문하지 않은 a와 연결되어 있으면 탐색
#             if computers[i][a] and not visited[a]:
#                 dfs(a)      
                
#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             # 네트워크 개수 +1
#             answer += 1
        
#     return answer



# 3. 팀원 풀이

# 봉준 (시간 1 ms/ 메모리 0.00390625 MB)
# 스택 사용

# def solution(n, comps):
#     def netw(node):
#         stack = [node]
#         while stack:
#             current = stack.pop()
#             if not state[current]:
#                 state[current] = True
#                 for i in range(n):
#                     if comps[current][i] == 1 and not state[i]:
#                         stack.append(i)

#     state = [False] * n
#     ans = 0
#     for i in range(n):
#         if not state[i]:
#             netw(i)
#             ans += 1
#     return ans



# 형수 (시간 0.61 ms/ 메모리 0.00390625 MB)
# 스택 사용

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def bfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            bfs(computers, visited, i)
            answer +=1
        i+=1
    return answer


# 프로그래머스 테스트 케이스에서는 대부분의 케이스에서 봉준 코드가 더 빠름
# 가설 1 케이스가 커지면 visited를 매번 검사하지 않는 봉준 코드가 더 빠르지 않을까? 
 
## case 1 (지난주에 테스트 한 케이스)
# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# 봉준 1ms
# 형수 0.61ms

## case 2 
# n = 5
# computers = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 1, 1, 1],
#     [0, 0, 0, 1, 1]
# ]

# 봉준 0.997ms 살짝 빨라짐
# 형수 1.0ms

## case 3
# n = 10
# computers = [
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
# ]

# 봉준 0.504ms 2배이상 빨라짐
# 형수 1.007ms

## case 4
# n = 20
# computers = [
#     [1] + [1 if j == i + 1 else 0 for j in range(1, 20)] for i in range(20)
# ]

# computers[19][18] = 1

# 봉준 0.886ms 
# 형수 1.092ms


# case 5 루프로 복잡성 추가
# n = 25
# computers = [
#     [1] + [1 if j == i + 1 else 0 for j in range(1, 25)] for i in range(25)
# ]

# computers[12][14] = computers[14][12] = 1
# computers[24][23] = 1

# 봉준 2.27ms
# 형수 1.523ms
# 형수 코드에 방문하지 않은 곳을 반복적으로 탐색하는 코드가 있음
# while 0 in visited:
#         if visited[i] ==0:
#             bfs(computers, visited, i)
#             answer +=1
#         i+=1
# 복잡성이 증가한 케이스에서 형수 코드가 더 빠름


# result = solution(n, computers)

# # 메모리 사용량과 종료 시간 측정
# end_time = time.time()
# end_memory = memory_usage()

# # 결과 출력
# print("네트워크 개수:", result)
# print("실행 시간: {:.6f} 초".format(end_time - start_time))
# print("메모리 사용량:", end_memory - start_memory, "MB")
