import itertools
import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cal = [list(map(int, input().split())) for _ in range(k)]

nPr = itertools.permutations(cal, k)
# print(list(nPr))
# [([3, 4, 2], [4, 2, 1]), ([4, 2, 1], [3, 4, 2])]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [[0]*(m+1)]
for _ in range(n):
    arr.append([0])

for i in range(1, n+1):
    arr[i] += data[i-1]

r, c, s = list(nPr)[0][0], list(nPr)[0][1], list(nPr)[0][2]

sx, sy = r-s, c-s
queue = [arr[sx][sy]]
visited = [[0]*(m+1) for _ in range(n+1)]

for i in range(4):
    nx, ny = sx+dx[i], sy+dy[i]
    # 일단 한방향 찾았으면 쭉 가는 코드 추가해야 됌
    if r-s <= nx <= r+s and c-s <= ny <= c+s and visited[nx][ny] == 0:
        queue.append(arr[nx][ny])
        arr[nx][ny] = queue.pop(0)
        visited[nx][ny] = 1