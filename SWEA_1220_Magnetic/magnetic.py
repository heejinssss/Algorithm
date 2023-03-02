T = 10

for test_case in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        cmp = ''
        for i in range(N):
            if arr[i][j] == 0:
                continue
            cmp += str(arr[i][j])
        for i in range(len(cmp)-1):
            if cmp[i]+cmp[i+1] == '12':
                cnt += 1

    print(f'#{test_case} {cnt}')