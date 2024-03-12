my_list = [2, 3, 5, 8, 5, 4, 2, 1, 3, 2, 2, 2, 1, 3]
counts = {}

for number in my_list:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

for number, count in counts.items():
    if count > 1:
        print(f"{number}는 {count}번 등장했습니다.")