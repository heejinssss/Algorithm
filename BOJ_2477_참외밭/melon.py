import sys
sys.stdin = open('input.txt', 'r')

size = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
direction = {1: 4, 2: 3, 3: 1, 4: 2}

# [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

for i in range(7):
    if lst[i][0] == direction[lst[i-1][0]]:
        continue
    minus = lst[i][-1] * lst[i-1][-1]
    break

lst.sort()

row = col = 0
for i in range(3):
    row += lst[i][-1]
    col += lst[i+3][-1]

print(size*((row//2)*(col//2)-minus))