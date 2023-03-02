T = int(input())
 
for test_case in range(1, T + 1):
 
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
 
    idx = N // 2 # 중앙 인덱스
    up = down = idx
 
    sum_ = 0
    for num in arr[idx]:
        sum_ += num # 중앙 값으로 시작
 
    for i in range(N//2):
        sum_ += sum(arr[up-1][1+i:N-1-i]) + sum(arr[down+1][1+i:N-1-i])
        up -= 1
        down += 1
 
    print(f'#{test_case} {sum_}')