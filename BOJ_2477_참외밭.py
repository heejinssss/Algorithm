import sys
sys.stdin = open('input.txt', 'r')

size = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
direction = {1: 4, 2: 3, 3: 1, 4: 2} # 반시계 방향으로 회전할 때, → ↑ ← ↓

# 반시계 방향의 흐름을 깨는 방향이 나왔을 때, 해당 부분이 잘린 모양
for i in range(7):
    if lst[i][0] == direction[lst[i-1][0]]:
        continue
    minus = lst[i][-1] * lst[i-1][-1]
    break

lst.sort()

row = col = 0
for i in range(3):
    row += lst[i][-1] # → ← 방향 모두 더하기
    col += lst[i+3][-1] # ↑ ↓ 방향 모두 더하기

print(size*((row//2)*(col//2)-minus))