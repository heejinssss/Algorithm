T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도
    ans90 = []
    for j in range(N):
        tmp = ''
        for i in range(N-1, -1, -1):
            tmp += str(arr[i][j])
        ans90 += [tmp]

    # 180도
    ans180 = []
    for i in range(N-1, -1, -1):
        tmp = ''
        for j in range(N-1, -1, -1):
            tmp += str(arr[i][j])
        ans180 += [tmp]

    # 270도
    ans270 = []
    for j in range(N-1, -1, -1):
        tmp = ''
        for i in range(N):
            tmp += str(arr[i][j])
        ans270 += [tmp]

    print(f'#{test_case}')
    for i in range(N):
        print(ans90[i], ans180[i], ans270[i])