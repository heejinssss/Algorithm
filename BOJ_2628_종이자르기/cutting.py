import sys
sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split()) # c = 10 r = 8
N = int(input()) # 자르는 횟수

row = []
col = []
for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        row += [temp[1]]
    else:
        col += [temp[1]]

row.sort()
col.sort()

row_lst = [0]+[1]*(r)
col_lst = [0]+[1]*(c)

row_idx = col_idx = 0
cnt_row = []
cnt_col = []

for num in row:
    cnt_row.append(row_lst[row_idx:num+1].count(1))
    row_idx = num+1
else:
    cnt_row.append(row_lst[row_idx:].count(1))

for num in col:
    cnt_col.append(col_lst[col_idx:num+1].count(1))
    col_idx = num+1
else:
    cnt_col.append(col_lst[col_idx:].count(1))

print(max(cnt_row) * max(cnt_col))