# 1. 문제 & 조건
# 모험가 수가 N명이고 공포도 값은 N 이하의 자연수로 주어짐
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야함
# 모든 모험가를 그룹에 넣을 필요 없음
# 여행 떠날 수 있는 그룹 수의 최댓값

# 2. 고민한 답
# 최대한 많은 그룹을 만든다 = 최소한의 인원으로 그룹을 만든다
# 그룹을 만들기 쉬운, 공포도가 낮은 순서로 정렬 후 그룹 만들기

n = int(input())
data = list(map(int, input().split))
data.sort()

group = 0
count = 0

for horror in data :
    count += 1
    if count >= horror :
       group += 1
       count = 0


print(group)
 
