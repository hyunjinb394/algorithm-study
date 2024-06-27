#https://softeer.ai/practice/6266

N, M = map(int,input().split())

names = [input() for _ in range(N)]
times = [input().split() for _ in range(M)]

names.sort()

answers = []
# 09 부터 18
for name in names:
    ans = [9,18]
    for time in times:
        if time[0] == name:
            if int(time[1]) in ans:
                ans.remove(int(time[1]))
            else: ans.append(int(time[1]))
            if int(time[2]) in ans:
                ans.remove(int(time[2]))
            else: ans.append(int(time[2]))
    ans.sort()
    answers.append([name,ans])

for i in range(len(answers)):
    print(f"Room {answers[i][0]}:")
    if len(answers[i][1]) == 0:
        print("Not available")
    else:
        print(f"{len(answers[i][1])//2} available:")
        for j in range(len(answers[i][1])//2):
            print(f"{(answers[i][1][2*j]):02}-{(answers[i][1][2*j+1]):02}")
    if i != len(answers)-1:
        print("-----")