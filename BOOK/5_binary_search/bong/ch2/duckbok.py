#떡 갯수 10^6개, 길이 2*10^9개 시간 제한 2초
#길이 관련해서는 시간복잡도 logm만 가능
#떡 갯수는 2nlogn 간당간당

# n,m = list(map(int,input().split(' ')))
# dlist = [int(input()) for _ in range(n)]
import numpy as np

n, m = 4, 25
dlist = [19, 15, 10, 17]

#시간 복잡도 m회. logm이상이므로 불가
def time_over_ans(n,m,dlist):
    dbox = [[0]*max(dlist) for _ in range(n)]           

    for i in range(n):
        dbox[i][:dlist[i]] = [1] *(dlist[i])        #n회

    dbox_np = np.array(dbox)
    array_transposed = np.transpose(dbox_np)

    ans = 0

    for i in range(max(dlist),0,-1):                #최대 m회
        ans += 1
        m -= sum(array_transposed[i-1])
        if m <= 0:
            break

    print(max(dlist)-ans)

#책 풀이(에 약간 추가)
def ans(m,dlist):
    start =0
    end = max(dlist)
    while (start <= end):                   #logm회
        total = 0
        mid = (start+ end)//2
        for x in dlist:                     #n회            ->nlogm회
            if x > mid:
                total += x -mid
        if total < m:
            end = mid -1

        #elif를 추가함. 이를 사용하지 않았다면 어떤 경우에도 nlogm회 실행. 하지만 이경우를 추가하는 경우 nlogm회 이전에 끝날수 있음. 하지만 최악의 약1.5배 길어질수도
        elif total == m:
            result = mid
            return result

        else:
            result = mid
            start = mid + 1
    return result 


print(ans(m,dlist))
