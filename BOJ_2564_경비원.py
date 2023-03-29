hor, ver = map(int, input().split()) # 블록 가로, 세로 길이
N = int(input()) # 동근이가 가야할 상점 개수

security = []
for _ in range(N):
    temp = list(map(int, input().split()))
    security.append(temp) # 상점 위치

donggeun = list(map(int, input().split())) # 동근이 위치

sum = 0
for item in security:
    temp = [item[0], donggeun[0]] # 상점의 방위, 동근이의 방위

    if temp == [1, 2] or temp == [2, 1]:
        min_1 = ver + item[1] + donggeun[1]
        min_2 = 2*hor + ver - item[1] - donggeun[1]
        min_ = min(min_1, min_2)

    elif temp == [1, 3] or temp == [3, 1]:
        min_ = item[1] + donggeun[1]

    elif temp == [1, 4] or temp == [4, 1]:
        min_ = hor - item[1] + donggeun[1]

    elif temp == [2, 3] or temp == [3, 2]:
        min_ = ver - item[1] + donggeun[1]

    elif temp == [2, 4] or temp == [4, 2]:
        min_ = ver + hor - item[1] - donggeun[1]

    elif temp == [3, 4] or temp == [4, 3]:
        min_1 = hor + item[1] + donggeun[1]
        min_2 = 2*ver + hor - item[1] - donggeun[1]
        min_ = min(min_1, min_2)

    elif temp == [1, 1] or temp == [2, 2] or temp == [3, 3] or temp == [4, 4]:
        min_ = abs(item[1] - donggeun[1])

    sum += min_

print(sum)