# 1. 문제
# 0 - 9까지의 문자열 S에 x 나 + 연산자를 넣음
# 연산은 연산자의 우선순위와 관계없이 왼쪽에서 오른쪽으로 진행
# 그 결과 만들어질 수 있는 가장 큰 수를 구하기 

# 2. 고민한 답
# 문자열 S에 0, 1 제외하고 x 연산자를 넣어주기

data = input()

result = int(data[0])
for number in range(1, len(data)) :
    num = int(data[number])
    if num <=1 or result <=1 :
        result += num
    else :
        result *= num

print(result)
