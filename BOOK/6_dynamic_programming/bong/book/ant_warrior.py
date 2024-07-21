#N이 3이상 100이하
#K는 1000이하
# 인접은 못뺐음.

n = int(input())
flist = list(map(int,input().split()))

def check(flist,N):
    f = [0]*100
    f[0] = flist[0]

    for i in range(N):
        if f[i-1] > f[i-2]+flist[i]:
            f[i]=f[i-1]
        else: f[i]=f[i-2]+flist[i]

    return f[N-1]
print(check(flist,n))
