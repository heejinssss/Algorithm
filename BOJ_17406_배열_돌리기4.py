import sys
sys.stdin = open('input.txt')

import itertools

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cal = [list(map(int, input().split())) for _ in range(k)]

nPr = itertools.permutations(cal, k)

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0]*(m+1)]
for _ in range(n):
    arr.append([0])

for i in range(1, n+1):
    arr[i] += data[i-1]

ans = []

cases = list(nPr)

for case in cases:
    arr_copy = []
    for lst in arr:
        arr_copy.append(lst[:])

    for nums in case:
        r, c, s = nums[0], nums[1], nums[2]

        k = 0
        visited = [[0] * (m+1) for _ in range(n+1)]

        while True:
            sx, sy = r-s+k, c-s+k
            if (1 <= sy-1 <= m and visited[sx][sy-1] == 1) and (1 <= sy+1 <= m and visited[sx][sy+1] == 1):
                break
            queue = [arr_copy[sx][sy]]

            for i in range(4):
                done = True
                while done:
                    nx, ny = sx+dx[i], sy+dy[i]
                    if r-s <= nx <= r+s and c-s <= ny <= c+s and visited[nx][ny] == 0:
                        queue.append(arr_copy[nx][ny])
                        arr_copy[nx][ny] = queue.pop(0)
                        visited[nx][ny] = 1
                        sx, sy = nx, ny
                    else:
                        done = False
            k += 1

    cmp = []
    for lst in arr_copy:
        cmp.append(sum(lst))
    ans += [cmp]

minV = 5001
for V in ans:
    if min(V) == 0:
        V.remove(0)
        minV = min(minV, min(V))

print(minV)