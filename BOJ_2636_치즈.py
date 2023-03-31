from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

cmp = [sum(arr, []).count(1)] # 한 사이클 돌 때마다 치즈 개수 누적 저장
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while arr != [[0]*m for _ in range(n)]: # 모든 치즈가 녹을 때까지 실행

    visited = [[0] * m for _ in range(n)]
    queue.append([0, 0])

    while queue:
        sx, sy = queue.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            # 공기를 만나면 좌표 저장, 방문 체크 완료 후 탐색 진행
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                # 치즈를 만나면 녹인 후, 방문 체크 완료
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visited[nx][ny] = 1

    cmp.append(sum(arr, []).count(1)) # 치즈 개수 저장
    cnt += 1

cmp.remove(0) # 모든 치즈가 녹은 후에 치즈 개수를 센 결과는 삭제

print(cnt)
print(cmp[-1])