bingo = [list(map(int, input().split())) for _ in range(5)] # 철수 빙고판

# 사회자가 가지고 있는 숫자 리스트
nums = []
for _ in range(5):
    num = list(map(int, input().split()))
    nums += num

def check(bingo, cnt): # 빙고 3개가 달성되었는가?

    # 행 기준
    for r in range(5):
        temp = []
        temp += bingo[r]
        if temp == [0, 0, 0, 0, 0]:
            cnt += 1
        if cnt == 3:
            return True

    # 열 기준
    for r in range(5):
        temp = []
        for c in range(5):
            temp.append(bingo[c][r])
        if temp == [0, 0, 0, 0, 0]:
            cnt += 1
        if cnt == 3:
            return True

    # 우하향 대각선 ↘
    temp = []
    for s in range(5):
        temp.append(bingo[s][s])
        if temp == [0, 0, 0, 0, 0]:
            cnt += 1
        if cnt == 3:
            return True

    # 우상향 대각선 ↗
    temp = []
    for s in range(4, -1, -1):
        temp.append(bingo[s][4-s])
        if temp == [0, 0, 0, 0, 0]:
            cnt += 1
        if cnt == 3:
            return True

    # 빙고 3개가 달성되지 않았을 경우
    return False

# 철수의 빙고판 숫자 중 사회자가 부른 숫자 개수
def zero(bingo):
    sum = 0
    for i in range(5):
        sum += bingo[i].count(0)
    return sum

cnt = 0

turn = 0
done = False # 마지막 for loop break 용도로 쓰일 변수
for std in nums:
    for i in range(5):
        if std in bingo[i]:
            bingo[i][bingo[i].index(std)] = 0
            turn += 1
            sum = zero(bingo)

            # 빙고 3개가 달성될 수 있는 가장 최소 조건이 12칸이므로
            if sum >= 12:
                ans = check(bingo, cnt)
                if ans == True:
                    done = True
                    break

    if done == True:
        print(turn)
        break