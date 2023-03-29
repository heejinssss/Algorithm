'''
1트에 '좌측 -> 중앙 <- 우측'으로 모이는 방법으로 하면 쉽게 풀릴 줄 알았으나 폭망
왜? 일단 경우의 수가 너무 많고... 정해진 기준을 잡기가 어렵기 때문에
중앙에서 가장 큰 값을 기준으로 잡고 좌우로 뻗는 형태로 다시 구현
'''

import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 기둥 개수
lst = [list(map(int, input().split())) for _ in range(N)] # 기둥 좌측 상단 좌표

lst.sort() # 기둥을 x축 기준으로 순서대로 정렬

# 가장 높은 기둥의 위치 찾기 (가장 높은 기둥을 가장 첫번째 기둥이라고 설정하고 탐색하면서 갱신하기)
max_ = lst[0][1]
idx = 0
for i in range(N):
    if max_ < lst[i][1]:
        max_ = lst[i][1]
        idx = i

std = lst[idx][1] # 제일 높은 기둥(기준) 넓이 미리 구해놓고 마지막에 추가할 예정

idx_ll = idx_rr = idx # while loop break용으로 쓰일 변수, 좌우의 포인터 값이 양끝을 가리키면 탐색 종료
idx_l = idx_r = idx # 계속 갱신할 인덱스 변수, 계산 끝나면 계산 끝난 기둥 인덱스로 이동
sum_l = 0 # 좌측 지붕 넓이
sum_r = 0 # 우측 지붕 넓이

while True:
    if idx_ll == 0:
        break

    temp_l = lst[:idx_ll] # 처음~현재 인덱스 기둥까지 [위치, 높이]를 temp에 저장
    # 마찬가지... temp 내에서 가장 높은 기둥의 위치 찾기
    max_l = temp_l[0][1]
    idx_l = 0
    for i in range(len(temp_l)):
        if max_l <= temp_l[i][1]:
            max_l = temp_l[i][1]
            idx_l = i
    
    # (현재 인덱스 기둥 ~ temp 내에서 가장 높은 기둥까지의 거리) * (temp 내에서 가장 높은 기둥의 값)
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

ans = std+sum_l+sum_r # 처음에 기준으로 잡은 가장 높은 기둥 넓이(높이 = 넓이) + 좌측 지붕 넓이 + 우측 지붕 넓이
print(ans)