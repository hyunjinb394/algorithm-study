#https://www.acmicpc.net/problem/10451
#재귀 함수 사용하면 좋을것으로 생각
# 재귀함수 부분 return을 지우면 왜 오류가 나는지 모르겠음......

t = 2
n1 = 8
n1_list = [3, 2, 7, 8, 1, 4, 5, 6]
n2 = 10
n2_list = [2, 1, 3, 4, 5, 6, 7, 9, 10, 8]

#cycle을 생성. 해당 위치로 가며, 그 위치에 있는 변수를 0으로 바꿈
#만일 그 위치가 이미 0이라면, 사이클이 끝났다고 인식 후 ans+1
def cycle(i, list, ans):
    if list[i] == 0:
        ans += 1
        return ans
    elif list[i] !=0:
        k = list[i] - 1
        list[i] = 0
        return cycle(k,list,ans)

def sol(n,list):
    ans = 0
    for i in range(n):
        if list[i]==0:
            continue
        else:
            ans = cycle(i, list, ans)
    return ans

print(sol(n2,n2_list))

