# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 복잡도 관련된거 없음
# nlist는 10^5개, n은 1000이하

# 만일 모든 수를 조합한다면 n(n+1)/2개를 생성 이후 정렬을 통해 확인. 따라서 시간이 n^2/2+nlogn 걸림.
# 이는 5*10^9+a만큼 시간이 걸림. => 약 500초 따라서 불가

def long_solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True)
    for i in range(len(numbers)):
        for j in range(i,0,-1):
            if int(numbers[j]+numbers[j-1])>int(numbers[j-1]+numbers[j]):
                numbers[j-1],numbers[j]=numbers[j],numbers[j-1]
            else:
                break
    return int(''.join(map(str,numbers)))


def solution(numbers):
    numbers = [str(i) for i in numbers]
    # x*3은 요소를 3번 반복 시킴
    # ex) 30 => 303030, 3=>333 이걸 str 방식으로 sort해서 해결
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


nlist = [3, 30, 34, 5, 9]
# nlist = map(int,input().split())

print(solution(nlist))


