#삽입정렬
#n번째의 숫자를 보며 앞숫자와 비교하여 순서를 배치
#시간복잡도 => 최소 N 최대 N*(N+1)/2 => 0(N^2)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i,0,-1):     #i번째 숫자가 그 앞의 숫자와 하나씩 비교하며 자신의 위치를 찾음
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break