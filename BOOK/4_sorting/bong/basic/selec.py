#선택 정렬
#각 위치에 와야하는 숫자를 하나씩 검사하여 찾는 방식
#시간복잡도 => 항상 N*(N+1)/2 => 0(N^2)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):         #0부터 9까지
    min_index = i                   #i번째 배열

    for j in range(i+1,len(array)):     # i+1부터 끝까지 모두 i번째 숫자와 비교
        if array[min_index] > array[j]: # i와 i+1을 비교
            min_index = j               # i와 j를 바꿈
    array[i],array[min_index] = array[min_index],array[i]   #i번째와 j번째 순서를 바꿈

print(array)
