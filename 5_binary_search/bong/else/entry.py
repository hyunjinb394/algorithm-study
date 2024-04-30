#https://school.programmers.co.kr/learn/courses/30/lessons/43238
#입국 심사 10^9명, 심사관 시간 10^9분, 심사관 10^5명.
# 심사관=m, 심사시간을 n이라고 했을때 mlogn으로 풀어야할듯
import math

n = 6
times = [7,10]

def sol(n,times):
    start = min(times)      # start =1로 놓으면 답이나오고, min(times)로 놓으면 답이 안나옴.......
    end = max(times)*n

    while start <=end:
        mid = (start + end)//2   

        human = 0                                  #통과한 사람
        for i in times:
            human += mid//i                        #human은 통과한 사람 총합
                                  
        if human > n:       #만일 human 크다면 통과할 사람 수를 줄여야함
            ans = mid
            end = mid -1
        elif human == n:     #만일 human 작다면 통과할 사람 수 늘려야함
            ans = mid
            return ans
        else:
            start = mid +1
    return ans

print(sol(n,times))