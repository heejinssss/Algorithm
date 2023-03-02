T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    lst = list(map(int, input().split()))

    cmp = []
    done = False
    for i in range(N):
        for j in range(N):
            if i+j+1 >= N:
                break
            else:
                cmp += [lst[i] * lst[i + j + 1]]
        if done:
            continue

    ans = []
    for num in cmp:
        for i in range(1, len(str(num))):
            if str(num)[i-1] <= str(num)[i]:
                continue
            break
        else:
            ans += [num]

    if ans == []:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {max(ans)}')