import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 기둥 개수
lst = [list(map(int, input().split())) for _ in range(N)] # 기둥 좌측 상단 좌표

lst.sort() # 기둥을 x축 기준으로 순서대로 정렬

sum = 0
l = 0
r = N-1

while True:
    # 왼쪽 기둥보다 오른쪽 기둥이 크다면
    if lst[l][1] <= lst[l+1][1]:
        sum += (lst[l+1][0] - lst[l][0]) * lst[l][1]
        l += 1
    # 왼쪽 기둥보다 오른쪽 기둥이 작다면? 큰 기둥이 나올 때까지 찾아야지
    else:
        i = 1
        done = False
        while True:
            # 왼쪽 기둥보다 큰 오른쪽 기둥이 나오면 중지
            if lst[l][1] < lst[l+i][1]:
                done = True
                break

            i += 1

            # 왼쪽 기둥보다 큰 오른쪽 기둥이 없다면, 그 중에서 큰 기둥을 찾아야지
            if l+i > N-1:
                temp = lst[l+1:]
                max_ = temp[0][1]
                max_idx = 0
                for k in range(1, len(temp)):
                    if max_ < temp[k][1]:
                        max_ = temp[k][1]
                        max_idx = k
                sum += lst[l][1] + (temp[max_idx][0]-lst[l][0]-1) * temp[max_idx][1]
                l += max_idx+1
                break

        # 왼쪽 기둥보다 큰 오른쪽 기둥을 찾았다면
        if done:
            sum += (lst[l + i][0] - lst[l][0]) * lst[l][1]
            l = l+i

    if r == l:
        sum += lst[l][1]
        print(sum)
        break
    elif l > 5:
        print(sum)
        break
    elif r < 0:
        print(sum)
        break

    # 오른쪽 기둥보다 왼쪽 기둥이 크다면
    if lst[r-1][1] >= lst[r][1]:
        sum += (lst[r][0] - lst[r-1][0]) * lst[r][1]
        r -= 1
    else:
        j = -1
        done = False
        while True:
            # 오른쪽 기둥보다 큰 왼쪽 기둥이 나오면 중지
            if lst[r+j][1] > lst[r][1]:
                done = True
                break

            j -= 1

            # 왼쪽 기둥보다 큰 오른쪽 기둥이 없다면, 그 중에서 큰 기둥을 찾아야지
            if r+j < 0:
                temp = lst[:r]
                max_ = temp[0][1]
                max_idx = 0
                for k in range(1, len(temp)):
                    if max_ < temp[k][1]:
                        max_ = temp[k][1]
                        max_idx = k
                sum += lst[r][1] + (lst[r][0]-temp[max_idx][0]-1) * temp[max_idx][1]
                r -= max_idx
                break

        # 오른쪽 기둥보다 큰 왼쪽 기둥을 찾았다면
        if done:
            sum += (lst[r][0]-lst[r+j][0]) * lst[r][1]
            r = r+j

    if r == l:
        sum += lst[l][1]
        print(sum)
        break
    elif l > 5:
        print(sum)
        break
    elif r < 0:
        print(sum)
        break