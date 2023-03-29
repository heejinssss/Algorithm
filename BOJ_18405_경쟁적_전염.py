n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

arr_tmp = sum(arr, [])
visited = [0]*(n**2)

sec = 0

# 0을 찾는 전략
while True:
    if s == 0:
        print(arr[x-1][y-1])
        break

    for si in range(n):
        for sj in range(n):
            if visited[si*n+sj] == 0:
                if arr_tmp[si*n+sj] != 0:
                    visited[si*n+sj] = 1

                else:
                    cmp = 1001
                    for k in range(4):
                        if 0 <= si+di[k] < n and 0 <= sj+dj[k] < n and arr_tmp[(si+di[k])*n+(sj+dj[k])] != 0:
                            ni, nj = si + di[k], sj + dj[k]
                            if arr_tmp[ni*n+nj] <= cmp:
                                cmp = arr_tmp[ni*n+nj]
                    if cmp != 1001:
                        arr[si][sj] = cmp
                        visited[si*n+sj] = 1

    sec += 1

    if arr_tmp.count(0) == 0 or sec == s:
        print(arr[x-1][y-1])
        break

    arr_tmp = sum(arr, [])