## 이진 탐색(Binary Search)

1. 동작 원리
* 범위를 절반씩 좁혀가면서 데이터를 탐색
* 범위를 좁히기 위해선 정렬이 필수적 
* 배열 전체의 중간값을 target과 비교해 왼쪽, 오른쪽 범위 선택
* 선택한 범위에서의 중간값과 target을 다시 비교
* 시간복잡도는 O(logN)

2. 구현 방법
   a. 재귀 함수 

```
def binary_search_recursion(target, start, end, data):
    if start > end:  # 재귀함수 종료 조건
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)

```

   b. 반복문 이용

```
def binary_search(data, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return data[mid]
        elif data[mid] < target: 
            start = mid + 1
        else: 
            end = mid -1

    return None # 찾는값 없으면 None

output = binary_search(data, target, 0, n-1)

```


3. 사용 예시