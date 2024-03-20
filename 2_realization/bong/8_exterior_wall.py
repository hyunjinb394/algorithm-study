#https://programmers.co.kr/learn/courses/30/lessons/60062


def solution(n, weak, dist):
    weak_dist = []
    total = 0
    for i in range(len(weak)-1):
        d = weak[i+1] - weak[i]
        weak_dist.append(d)
        total += d
    weak_dist.append(n - total)
    print(weak_dist)

    



    # return answer







class pro1():
    n = 12
    weak = [1,5,6,10]
    dist = [1,2,3,4]

class pro2():
    n =12
    weak = [1,3,4,9,10]
    dist = [3,5,7]

solution(pro1.n,pro1.weak,pro1.dist)