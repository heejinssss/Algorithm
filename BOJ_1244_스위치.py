N = int(input()) # 스위치 개수
lst = list(map(int, input().split())) # 스위치 on/off 상태
std = int(input()) # 학생 수

for _ in range(std):

    sex, num = map(int, input().split()) # 성별, 뽑은 수

    idx = num-1 # 실제 스위치 위치값보다 인덱스값이 1만큼 작기 때문

    # 남학생이면
    if sex == 1:
        # 뽑은 수의 배수 위치에 해당하는 스위치 on/off
        while idx <= N-1:
            if lst[idx] == 0:
                lst[idx] = 1
            else:
                lst[idx] = 0
            idx += num

    # 여학생이면
    elif sex == 2:
        i = 0
        # 뽑은 수 위치에 해당하는 스위치를 기준으로 가장 큰 좌우 대칭 범위 찾아서 스위치 on/off
        while 0 <= idx-i and N-1 >= idx+i and lst[idx-i] == lst[idx+i]:
            if lst[idx-i] == lst[idx+i] == 1:
                lst[idx-i] = lst[idx+i] = 0
            else:
                lst[idx-i] = lst[idx+i] = 1
            i += 1

cnt = 1
for n in lst:
    if cnt % 20 == 0: # 20번째마다 줄 바꿈
        print(n)
        cnt += 1
    else:
        print(n, end= ' ')
        cnt += 1