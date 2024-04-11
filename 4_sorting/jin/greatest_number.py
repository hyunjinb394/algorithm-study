# 1. 문제
# numbers는 0 또는 양의 정수가 담긴 배열
# 배열 안에 숫자를 재배치 해서 만들 수 있는 가장 큰 수 return
# numbers 길이 10^5 이하
# 답은 문자열로 바꿔서 return 

# 2. 고민한 답안 
# 틀림

def solution(numbers):
    # 배열의 수를 string으로 합치기
    numbers = list(map(str, numbers))
    
    # 원소는 1000 미만
    # 3배로 문자열을 늘린 뒤 문자열 대소비교
    # 왼쪽부터 차례대로 숫자 비교
    numbers.sort(key=lambda x: x*3, reverse=True)

    largest = ''.join(numbers)
    
    # string으로 합친 수 중에 제일 큰 수를 string으로 return
    return largest

# numbers_arr = [3, 20, 555]
# print(solution(numbers_arr))

# 3. 틀린 지점
# 테스트 케이스 11번 모두 0일때 pass 못함

def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*3, reverse=True)

    largest = ''.join(numbers)
    # 000 -> 0으로 바꾸기 위해
    # int로 바꾸고 str로 출력
    return str(int(largest))

# 또는 0인 케이스만 따로 빼주기

def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*3, reverse=True)

    largest = ''.join(numbers)

    if largest[0] == '0' :
        return '0'
    
    return largest