N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0 # 섭취한 먹이 수 (성장할 때마다 초기화 예정)
time = 0
size = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어 초기 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sx, sy = i, j

def bfs(sx, sy, size):
    visited = [[0]*N for _ in range(N)]
    ans = [[0] * N for _ in range(N)]

    queue = [[sx, sy]]
    visited[sx][sy] = 1 # 초기 위치 방문 완료 표시
    cmp = [] # [현재 위치부터 먹을 수 있는 먹이까지의 거리, x, y]

    while queue:
        cx, cy = queue.pop(0)
        
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] <= size:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    ans[nx][ny] = ans[cx][cy] + 1
                    if arr[nx][ny] < size and arr[nx][ny] != 0:
                        cmp.append([ans[nx][ny], nx, ny])
                        
    # 거리 기준 오름차순, x값 기준 오름차순 (작은 수부터), y값 기준 오름차순 (작은 수부터)
    cmp = sorted(cmp, key=lambda x: (x[0], x[1], x[2]))
    return cmp

while True:
    mom = bfs(sx, sy, size)

    if not len(mom):
        break

    t, nx, ny = mom.pop(0)
    time += t
    cnt += 1

    arr[sx][sy], arr[nx][ny] = 0, 0 # 출발한 위치와, 물고기 먹은 위치 0으로 초기화
    sx, sy = nx, ny # 물고기를 먹은 자리로 현재 위치를 초기화

    if cnt == size: # 섭취한 먹이 수가 현재 크기와 같다면
        size += 1 # 성장
        cnt = 0 # 섭취한 먹이 수 초기화

print(time)