T = int(input())

for test_case in range(1, T+1):

    N1, N2 = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    if N1 < N2:
        cmp = []
        for j in range(0, N2-N1+1):
            ans = []
            for i in range(N1):
                if i+j > N2:
                    continue
                ans += [lst1[i]*lst2[i+j]]
            cmp += [sum(ans)]

    elif N1 > N2:
        cmp = []
        for j in range(0, N1-N2+1):
            ans = []
            for i in range(N2):
                if i+j > N1:
                    continue
                ans += [lst2[i]*lst1[i+j]]
            cmp += [sum(ans)]

    print(f'#{test_case} {max(cmp)}')