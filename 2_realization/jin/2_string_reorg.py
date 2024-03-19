# 1. 문제
# 알파벳 대문자와 0 - 9 로 구성된 문자열이 주어짐
# 모든 알파벳을 오름차순으로 이어 출력 후 모든 숫자를 더한 값을 이어 출력
# 첫 줄에 하나의 문자열 S가 주어짐 (1 ≤ S의 길이 ≤ 10,000 )

# 2. 고민한 답안

S = input()

# 알파벳이면 배열에 저장
# 숫자면 합을 구함
string = []
total = 0

for i in S:
    if i.isalpha():
        string.append(i)
    else : 
        total += int(i)

# 알파벳 배열을 오름차순으로 정렬하고 숫자를 문자열로 더해줌
string.sort()

result = ''.join(string) + str(total)

print(result)
