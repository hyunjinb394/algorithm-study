#https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 풀이
# 우선 압축 최대 길이는 문자열 전체 길이 나누기 2 = l
# 1부터 l까지 한개씩 문자열 만들어 보기

def solution(s):
    # 문자열 길이 나누기 2
    l = int(len(s)/2)
    answer = len(s)

    for i in range(1,l+1):
        zip_string = ''                 #생성될 문자열
        prev = s[0:i]                   #처음 반복될
        count = 1                       #횟수 확인
        for a in range(i, len(s),i):
            if prev == s[a:a+i]:        #반복할 숫자와 바로다음 오는 숫자 비교
                count +=1               #맞다면 +1
            else:
                zip_string += str(count) + prev if count > 1 else prev  # 문자열에 추가
                prev = s[a:a+i]         #반복할 숫자 재생성             #'''오류 발견: a:a+i가 아닌 i:a+i도 답으로 처리. 하지만 이는 틀림'''
                count = 1
        zip_string += str(count) + prev if count > 1 else prev
        answer = min(answer, len(zip_string))                           #최소값 비교 후 결정
    return answer

print(solution('agagagagda'))