import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 기둥 개수
lst = [list(map(int, input().split())) for _ in range(N)] # 기둥 좌측 상단 좌표

lst.sort() # 기둥을 x축 기준으로 순서대로 정렬

max_ = lst[0][1]
idx = 0
for i in range(N):
    if max_ < lst[i][1]:
        max_ = lst[i][1]
        idx = i

std = lst[idx][1] # 제일 높은 기둥(기준) 넓이

idx_ll = idx_rr = idx
idx_l = idx_r = idx
sum_l = 0
sum_r = 0

while True:
    if idx_ll == 0:
        break

    temp_l = lst[:idx_ll]
    max_l = temp_l[0][1]
    idx_l = 0
    for i in range(len(temp_l)):
        if max_l <= temp_l[i][1]:
            max_l = temp_l[i][1]
            idx_l = i

    sum_l += abs(lst[idx_ll][0]-temp_l[idx_l][0])*temp_l[idx_l][1]
    idx_ll = idx_l

while True:
    if idx_rr == N-1:
        break

    temp_r = lst[idx_rr+1:]
    max_r = temp_r[0][1]
    idx_r = 0
    for i in range(len(temp_r)):
        if max_r <= temp_r[i][1]:
            max_r = temp_r[i][1]
            idx_r = i

    sum_r += abs(lst[idx_rr][0]-temp_r[idx_r][0])*temp_r[idx_r][1]
    idx_rr = idx_rr+idx_r+1

ans = std+sum_l+sum_r
print(ans)
