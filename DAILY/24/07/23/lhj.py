# 666, 1666, ...5666, 6660, 6661, 6662...
n=int(input())
cnt = 0
result=666
 
while True:
    if '666' in str(result):
        cnt+=1
    if cnt == n:
        break
    result+=1

print(result)