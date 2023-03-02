T = int(input())

for test_case in range(1, T + 1):

    dummy, hoxy = map(int, input().split())
    score = list(map(int, input().split()))

    score.sort(reverse=True)

    ans = sum(score[0:hoxy])

    print(f'#{test_case} {ans}')