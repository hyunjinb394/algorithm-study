# 1. 문제
# 스택 연습문제 / 프로그래머스 / 올바른 괄호 / lv 2 
# "()()" 또는 "(())()" 는 올바른 괄호
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때
# 문자열 s가 올바른 괄호이면 true를. 올바르지 않은 괄호이면 false를 return 

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어짐

# 2. 고민한 답안

def solution(s):
    stack = []
    for i in s :
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    if stack != []:
        return False

    return True


# 3. 효율적인 답안

def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            # 빈스택에서 pop을 하게 되면 IndexError 발생
            # IndexError 발생시 except IndexError : 실행
            except IndexError:
                return False

    # 스택의 길이가 0이면 True, 0이 아니면 False 반환
    return len(st) == 0