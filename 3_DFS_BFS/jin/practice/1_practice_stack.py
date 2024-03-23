# 1. 문제
# 스택 연습문제 / 프로그래머스 / 같은 숫자는 싫어 / lv 1 
# 배열 arr의 각 원소는 숫자 0부터 9까지
# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 배열 arr의 원소들의 순서를 유지


# 제한사항
# 배열 arr의 크기 : 1,000,000 이하의 자연수
# 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

# 2. 고민한 답안
def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])            
    return answer

# 3. 효율적인 답안
# 리스트 슬라이싱은 빈 리스트일때도 빈 리스트 반환
# 첫 번째 원소 처리 시 발생하는 인덱스 에러 방지

def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        # a의 마지막 원소와 i가 동일한 경우 아래의 코드를 실행하지 않고
        # 다음 i로 넘어가 반복 실행
        a.append(i)
    return a
