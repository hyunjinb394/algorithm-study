# 1. 문제 이해
# N개의 회의실, 9시부터 18시까지만 사용가능, 시간단위
# 회의시간은 겹칠 수 없다
# 시간이 0인 회의는 없다
# M개의 회의에 대한 정보가 주어지면 비어있는 시간대를 정리해 출력
# 1 ≤ N ≤ 50, 1 ≤ M ≤ 100
# 회의실 이름 r, 시작시간 s, 종료시간 t
# 회의실 이름을 오름차순 출력


# 2. 문제 풀이

n, m = map(int, input().split())
room_name = [input().strip() for _ in range(n)]
meetings = []

for i in range(m):
    r, s, t = input().split()
    s = int(s)
    t = int(t)
    meetings.append((r, s, t))

room_name.sort()

schedule = {room: [] for room in room_name}

for meeting in meetings:
    r, s, t = meeting
    schedule[r].append((s, t))

for index, room in enumerate(room_name):
    print(f"Room {room}:")
    if not schedule[room]:
        print("1 available:")
        print("09-18")
    else:
        schedule[room].sort()
        ok_time = []
        current_time = 9

        for (start, end) in schedule[room]:
            if current_time < start:
                ok_time.append((current_time, start))
            current_time = end

        if current_time < 18:
            ok_time.append((current_time, 18))

        if not ok_time:
            print("Not available")
        else:
            print(f"{len(ok_time)} available:")
            for (start, end) in ok_time:
                print(f"{start:02d}-{end:02d}")

    if index < len(room_name) - 1:
        print("-----")

