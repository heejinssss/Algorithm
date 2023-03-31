from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    # 연합된 국가 담기 ===================================================
    union = [(i, j)]
    count = arr[i][j]   # 총 연합된 국가 수

    # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기
    while queue:
        sx, sy = queue.popleft()
        for d in range(4):
            nx = sx + dx[d]
            ny = sy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and l <= abs(arr[nx][ny] - arr[sx][sy]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기
                union.append((nx, ny))
                visited[nx][ny] = 1
                queue.append((nx, ny))
                count += arr[nx][ny]

    # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산
    for x, y in union:
        arr[x][y] = count // len(union)

    return len(union)

result = 0  # 인구 이동이 발생하는 일수

# 1. 인구 이동이 없을 때까지 반복
while True:
    visited = [[0] * n for _ in range(n)]
    done = False

    # 2. 모든 곳을 bfs로 방문하여 연합 진행
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    done = True

    # 3. 지금까지 인구 이동이 없는 경우, 그만
    if not done:
        break
    result += 1

print(result)