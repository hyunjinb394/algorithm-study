# 시간 1초, 메모리 128mb
# 최대 10^5개 따라서 N^2불가, NlogN은 넉넉하게 가능 메모리는 신경 x

n = int(input("학생 수: "))
nlist = [input().split() for _ in range(n)]

#lamda는 sorted()함수의 변수를 설정해줌. 변수를 key가 배열x의[1]에 해당한다고 표기함으로서 아래처럼 사용가능.
nlist = sorted([[l[0],int(l[1])] for l in nlist],key = lambda x: x[1])

print(nlist)