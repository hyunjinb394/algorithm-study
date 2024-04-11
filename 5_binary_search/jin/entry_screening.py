# 1. 문제

# 2. 고민한 답안
# 왜 이진탐색 문제로 출제된 것인지 이해가 되지x
# (지난시간 // 심사하는데 걸린시간) = 각심사관이 심사를 끝낸 인원
 

def solution(n, times):
    answer = 0
    low = 0
    high = max(times) * n   # 모든 인원 검사에 최대로 걸리는 시간

    while low <= high:

        # 입국심사 최소 시간
        # 처음에는 가장 오래 걸리는 심사관의 시간과 가장 적게 걸리는 심사관의 시간의 평균으로
        mid = (low + high) //2

        count = 0
        for time in times:
            count = count + mid // time

            # 모든 인원을 검사 가능 하면 break
            if count >= n:
                break

        # 모든 인원을 검사 가능하면 answer를 지금으로 업데이트 해주고
        # 최소 시간을 줄여나간다. high가 줄어들 수 있는 이상 최소값이 더 있을 수 있다.
        if count >= n :
            high = mid - 1
            answer= mid
        # 모든인원을 검사 할수 없으면 최소 시간을 늘린다.
        else :
            low = mid +1

    return answer


# 3. 효율적인 답안