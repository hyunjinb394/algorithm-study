k = int(input('k초 : '))
food_t = list(map(int,input('음식 먹는데 걸리는 시간 : ').split()))

def solution(food_times, k):
    if sum(food_times) < k: answer = -1
    
    

    return answer

print(solution(food_t, k))