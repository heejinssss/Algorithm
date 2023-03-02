T = int(input())

for test_case in range(1, T + 1):

    std, submit = map(int, input().split())
    substd = list(map(int, input().split()))

    ans = []
    for num in range(std):
        if num+1 in substd:
            continue
        ans += [num+1]

    ans.sort()

    print(f'#{test_case}', end = ' ')
    print(*ans)