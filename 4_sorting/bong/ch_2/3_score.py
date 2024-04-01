# 시간 1초, 메모리 128mb
# 최대 10^5개 따라서 N^2불가, NlogN은 넉넉하게 가능 메모리는 신경 x

n = int(input("학생 수: "))
nlist = [input().split() for _ in range(n)]

nlist = sorted([[l[0],int(l[1])] for l in nlist],key = lambda x: x[1])

print(nlist)