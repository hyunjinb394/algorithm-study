# 1. 문제
# 주어진 순열의 인덱스 +1 값으로 그래프가 연결됨
# 첫 줄에 T개의 테스트 케이스 주어짐
# 둘째줄에 순열 크기 주어지고 그 다음줄에 순열이 주어짐
# 순열 사이클 개수 출력

# 2. 고민한 답안 (메모리 31212 KB 시간 584 ms)
# 네트워크랑 비슷
# 하나의 노드에서 깊게 탐색하는 풀이로 DFS 사용
# T : 테스트 케이스 수
# n : 순열 길이
# arr : 순열  정보 저장 리스트
# visited : 방문한 노드 체크하는 함수

T = int(input())
arr = [0]

def find_cycle(now) :
    visited[now] = 1
    # 현재 위치에 있는 인덱스의 값
    next = arr[now]
    # next를 방문하지 않았다면
    # 사이클 찾기
    if visited[next] == 0 :
        find_cycle(next)
    return

for _ in range(T):
    n = int(input())
    # 인덱스를 맞추기 위해서 리스트 맨앞에 0 추가
    arr = list(map(int, input().split()))
    arr.insert(0,0)

    # 사이클 개수 
    cnt = 0
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        # 방문하지 않았다면
        if visited[i] == 0:
            # 함수 호출 후 사이클 찾기
            find_cycle(i)
            cnt += 1
    print(cnt)
