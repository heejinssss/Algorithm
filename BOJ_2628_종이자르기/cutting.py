import sys
sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split())
N = int(input()) # 자르는 횟수

# 점선 번호 리스트로 저장
row = []
col = []
for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        row += [temp[1]]
    else:
        col += [temp[1]]

row.sort() # 점선 번호 순서대로 정렬
col.sort()

row_lst = [0]+[1]*(r) # 인덱스 번호와 실제 점선 번호 1대1 대응
col_lst = [0]+[1]*(c)

row_idx = col_idx = 0
cnt_row = []
cnt_col = []

for num in row:
    cnt_row.append(row_lst[row_idx:num+1].count(1)) # 잘린 부분 ~ 점선 번호까지 칸 수 세기
    row_idx = num+1
else:
    cnt_row.append(row_lst[row_idx:].count(1)) # for loop가 완전하게 종료되면 잘린 부분 ~ 마지막 번호까지 칸 수 세기

for num in col:
    cnt_col.append(col_lst[col_idx:num+1].count(1))
    col_idx = num+1
else:
    cnt_col.append(col_lst[col_idx:].count(1))

print(max(cnt_row) * max(cnt_col)) # 가로, 세로 가장 긴 길이쌍 곱하기