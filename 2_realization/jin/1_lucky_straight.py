# 1. 문제
# 점수 N을 자릿수를 기준으로 반으로 나눔
# 왼쪽 오른쪽 자릿수의 합이 동일하면 기술 사용 가능
# 기술 사용 가능하면 LUCKY, 사용할 수 없으면 READY를 출력
# N은 정수 (10 ≤ N ≤ 99,999,999)
# 자릿수는 반드시 짝수인 값이 입력됨

# 2. 고민한 답안
# 입력된 점수를 리스트로 받기
N = input()
data = list(map(int, N))

# 리스트 길이의 반 기준으로 가운데 구하기
m = len(data) // 2

# 왼쪽 오른쪽 더한 값이 같으면 LUCKY, 다르면 READY 출력
if sum(data[:m]) == sum(data[m:]) :
    print("LUCKY")
else :
    print("READY")


# 3. 효율적인 답안
    
N = input()


left_sum = 0
right_sum = 0

mid = len(N) // 2

# 리스트 슬라이싱 대신 for문으로 문자열 인덱스를 사용
# 각 자리 수를 순회하며 합산
# 리스트로의 변환 과정 줄일 수 있음

for i in range(mid):
    left_sum += int(N[i])
    right_sum += int(N[mid + i])


if left_sum == right_sum :
    print("LUCKY")
else :
    print("READY")