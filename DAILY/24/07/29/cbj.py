# https://www.acmicpc.net/problem/1024
N, L = map(int, input().split())

'''
x=첫번째 수, l=길이
N = (x+(x+l-1))*l/2 = (2x+l-1)*l/2 = lx + l**2/2 - l/2
lx = N-l(l+1)/2 
'''

for l in range(L,101):
    lx = N - (l*(l+1))//2
    if lx % l == 0:
        x = lx // l
        if x + 1 >= 0:
            print(*(i for i in range(x+1,x+l+1)))
            exit()

print(-1)