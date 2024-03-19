k = int(input('k초 : '))
food_t = list(map(int,input('음식 먹는데 걸리는 시간 : ').split()))

def solution(food_times, k):
    if k > sum(food_times):
        return -1
    n = 0
    while k > 0:
        if food_times[n] == 0:
            n = n+1
            k = k+1
        else:
            food_times[n] -= 1

        n += 1
        k -= 1

        if n == len(food_times):
            n = 0

    ans = n    
    return ans

print(solution(food_t, k))