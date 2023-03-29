def solution(rows, columns, queries):
    answer = []

    arr = [[0] * (columns + 1) for _ in range(rows + 1)]
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = num
            num += 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for lst in queries:
        queue = []
        visited = [[0] * (columns + 1) for _ in range(rows + 1)]
        si, sj = lst[0], lst[1]
        queue.append(arr[si][sj])

        minV = min(queue)
        done = False

        for k in range(4):
            while True:
                ni, nj = si + di[k], sj + dj[k]
                if lst[0] <= ni <= lst[2] and lst[1] <= nj <= lst[3] and visited[ni][nj] == 0:
                    queue.append(arr[ni][nj])
                    arr[ni][nj] = queue.pop(0)
                    minV = min(minV, queue[0])
                    visited[ni][nj] = 1
                    si, sj = ni, nj
                else:
                    done = True
                    break

            if done:
                continue

        answer.append(minV)

    return answer
