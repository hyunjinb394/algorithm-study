# 1. 문제
# n : 수열 속 수의 개수, 1 ≤ N ≤ 500
# 수열의 내림차순으로 정렬된 결과를 공백 추가해 출력

# 2. 고민한 답안

n = int(input())

array = []

for i in range(n) :
    array.append(int(input()))

array.sort(reverse=True)
print(' '.join(map(str, array)))    


# 3. sort vs sorted 
# 둘의 시간 복잡도는 nlogn으로 동일
# sort가 직접적으로 리스트를 정렬
# sorted는 메모리를 사용해서 새로운 리스트를 반환
# sorted는 모든 자료형에서 사용가능, sort는 리스트에만 사용가능


n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

sorted_array = sorted(array, reverse=True)
print(' '.join(map(str, sorted_array)))


# 4. 효율적인 답안
# 리스트 컴프리핸션

n = int(input())
array = [int(input()) for _ in range(n)]
sorted_array = sorted(array, reverse=True)
print(' '.join(map(str, sorted_array)))