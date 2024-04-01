#제한시간 1초, 메모리제한 128mb
#500개이하의 숫자 배열. O(N^3)까지도 가능할듯. 시간복잡도 상관 ㄴ, 공간도 상관 ㄴ

n = int(input("수열의 수: "))
nlist = [int(input()) for _ in range(n)]

# n = 3
# nlist = [15,27,12]

ans = nlist[:]              #동일한 리스트 객체가 아닌 새로운 복사본 생성
ans.sort(reverse = True)
print(ans)
print(nlist)