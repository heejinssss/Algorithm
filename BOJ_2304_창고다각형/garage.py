import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 기둥 개수
lst = [list(map(int, input().split())) for _ in range(N)] # 기둥 좌측 상단 좌표

lst.sort() # 기둥을 x축 기준으로 순서대로 정렬

# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

sum = 0
l = 0
r = N-1

while True:
    if l == r:
        print(sum)
        break

    if lst[l][1] <= lst[l+1][1]:
        print(1)
        sum += (lst[l+1][0] - lst[l][0]) * lst[l][1]
    else:
        print(2)
        sum += lst[l][1]+(lst[l+1][0]-lst[l][1])*lst[l+1][1]

    if lst[r][1] >= lst[r-1][1]:
        print(3)
        sum += (lst[r][0] - lst[r-1][0]) * lst[r][1]
    else:
        print(4)
        sum += lst[r][1] + (lst[r][0] - lst[r-1][0]) * lst[r-1][1]
    l += 1
    r -= 1