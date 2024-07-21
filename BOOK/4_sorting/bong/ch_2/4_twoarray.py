#시간 2초, 메모리 128mb
#10^5배열 2개, 10^5번 바꿀수 있음

#2번 sort하고 비교하면 => 2NlogN + N회 따라서 ㄱㅊ

# N,K = map(int,input().split())
# nlist = [input().split() for _ in range(N)]

N,K = 5,3
nlist =[[1,2,5,4,3],[5,5,6,6,5]]

a = nlist[0]
b = nlist[1]

a.sort()
b.sort(reverse=True)

for i in range(K):
    if b[i]>a[i]:
        a[i],b[i] = b[i],a[i]

ans = sum(a)
print(ans)


