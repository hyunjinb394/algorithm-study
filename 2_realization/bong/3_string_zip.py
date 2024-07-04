#https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 풀이
# 우선 압축 최대 길이는 문자열 전체 길이 나누기 2 = l
# 1부터 l까지 한개씩 문자열 만들어 보기
def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        zip_string = ''
        prev = s[0:i]
        count = 1
        for a in range(i,len(s),i):
            if prev == s[a:a+i]:
                count +=1
            else:
                zip_string += str(count) +prev if count >1 else prev
                prev = s[a:a+i]
                count = 1
        zip_string += str(count) + prev if count > 1 else prev
        print(zip_string)
        answer = min(answer, len(zip_string))    
        
    return answer

print(solution("ababcdcdababcdcd"))