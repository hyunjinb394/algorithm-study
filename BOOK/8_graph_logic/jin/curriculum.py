# 1. 문제 이해
# 어떤 강의는 선수강의를 들어야만 들을 수 있음
# N개의 강의를 들으려고 하고 동시에 여러 강의를 들을 수 있을때
# N개의 강의를 수강하는데 걸리는 최소 시간을 각각 출력
 

# 2. 문제 풀이 (10ms)
# 루트가 아닌거 체크해두기
# 위상정렬...? 그게 멀까.. >> MD 파일 참고


from collections import deque

# 입력 받기
N = int(input()) 
prev_list = [[] for _ in range(N + 1)] # 노드별 선수강의 저장
in_degree = [0] * (N + 1) # 노드 별 필요한 선수강의 수 저장
time = [0] * (N + 1)

# 선수강의 리스트 세팅 & 진입 차수 계산
for i in range(1, N + 1):
    data = list(map(int, input().split()))[:-1]  # -1로 끝나는 입력 받기
    time[i] = data[0]  # 각 강의의 시간 저장
    in_degree[i] += len(data[1:])  # 진입 차수 증가
    for x in data[1:]:
        prev_list[x].append(i) # 선수강의 저장하는 리스트에 추가

# 위상 정렬 함수 작성
def topology_sort():
    start_time = time_now() # 시간 측정
    result = [0] * (N + 1) 
    q = deque()  

    # 차수가 0인 노드를 찾아라 
    # 0인 노드를 큐에 추가
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()

        # 현재 노드 주변의 이웃 노드(다음 강의)의 진입 차수 감소
        for next_lecture in prev_list[now]:
            in_degree[next_lecture] -= 1
            # 각각의 이웃 강의에 대해서 더 큰 값으로 갱신
            result[next_lecture] = max(result[next_lecture], result[now] + time[next_lecture])
            # 차수가 0 이되면 q에 추가 -> 차수가 0이되는 순서대로 q에 들어감 
            if in_degree[next_lecture] == 0:
                q.append(next_lecture) 

    # 결과 출력
    for i in range(1, N + 1):
        print(result[i])

    end_time = time_now()  
    print("실행시간 :", "{:.10f}".format(end_time - start_time), "초") 


def time_now():
    import time
    return time.time()

# 위상 정렬 함수 호출
topology_sort()