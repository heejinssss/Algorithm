T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # ↑ → ← ↓
    # for di, dj in ((-1,0), (1,0), (0,-1), (0,1)) 형태도 가능
    drpx = [-1, 0, 1, 0]
    drpy = [0, 1, 0, -1]

    # ↗ ↖ ↙ ↘
    # for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)) 형태도 가능
    drmx = [-1, -1, 1, 1]
    drmy = [1, -1, -1, 1]

    ans = []

    # + 모양으로
    for i in range(N):
        for j in range(N):
            sum = 0
            center = arr[i][j]
            for k in range(4): # 네 방향
                si, sj = i, j # 중앙 값 초기화
                for _ in range(M-1): # M-1만큼 반복
                    ni, nj = si+drpx[k], sj+drpy[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        sum += arr[ni][nj]
                        si, sj = ni, nj
            ans += [sum + center] # [i, j] 기준 퇴치 가능한 파리 수 저장

    # X 모양으로
    for i in range(N):
        for j in range(N):
            sum = 0
            center = arr[i][j]
            for k in range(4): # 네 방향
                si, sj = i, j # 중앙 값 초기화
                for _ in range(M-1): # M-1만큼 반복
                    ni, nj = si+drmx[k], sj+drmy[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        sum += arr[ni][nj]
                        si, sj = ni, nj
            ans += [sum + center] # [i, j] 기준 퇴치 가능한 파리 수 저장

    print(f'#{test_case} {max(ans)}')