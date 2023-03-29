from sys import stdin

c, r = map(int, stdin.readline().split()) # 입력 속도 향상
# c, r = map(int, stdin.readline().split()) 로 입력 받으면 시간 초과(로 4트)
N = int(input())

x = y = cnt = pivot = 1

if N == 1: # 대기 번호가 1일 때
    print(x, y)
elif N > r * c: # 대기 번호가 좌석 수보다 클 때
    print(0)
else:
    done = False # while loop break할 때 사용할 변수 선언
    while True: # 1번 while loop

        while y != r: # 2번 while loop, 위쪽 벽에 닿을 때까지
            y += 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break # 2번 while loop break

        if done:
            break # 1번 while loop break

        while x != c: # 3번 while loop, 오른쪽 벽에 닿을 때까지
            x += 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break # 3번 while loop break

        if done:
            break # 1번 while loop break

        while y != pivot: # 4번 while loop, 아래쪽 벽에 닿을 때까지
            y -= 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break # 4번 while loop break

        if done:
            break # 1번 while loop break

        while x != pivot+1: # 5번 while loop, 왼쪽 벽에 닿을 때까지
            x -= 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break # 5번 while loop break

        if done:
            break # 1번 while loop break

        # 한 사이클을 돌 때마다
        r -= 1
        c -= 1
        pivot += 1