n = int(input('동전 갯수 입력 : '))
coin = list(map(int,input('동전 입력 : ').split()))

coin.sort()

num_list = [i for i in range(1, sum(coin)+1)]

for n in num_list:
    ans = n
    
    