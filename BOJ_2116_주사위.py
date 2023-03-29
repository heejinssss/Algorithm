dict_ = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0} # 주사위의 마주보고 있는 값의 인덱스 쌍 (불변)

N = int(input()) # 주사위 개수
dice = [list(map(int, input().split())) for _ in range(N)]
pivot = dice[0][:] # 깊은 복사 시도

cmps = []
for num in pivot:
    # 첫번째 주사위의 밑면을 정한 후, 윗면 인덱스를 dict_에서 찾아 해당 값을 cmp에 저장
    cmp = [pivot[dict_[pivot.index(num)]]]
    for i in range(0, N):
        # i번째 주사위 윗면 값과 동일한 값을 i+1번째 주사위에서 찾은 후, 윗면 인덱스를 dict_에서 찾아 해당 값을 cmp에 추가
        cmp.append(dice[i][dict_[(dice[i]).index(cmp[-1])]])
    cmps.append(cmp)

''' cmps 값
[[4, 2, 6, 1, 5, 1], # 이게 주사위 윗면 값 (1트)
 [6, 3, 5, 2, 3, 4], # 2트... 이런 식으로 6트까지 (왜? 주사위는 6면이니까)
 [5, 1, 4, 3, 2, 6],
 [3, 6, 2, 5, 1, 5],
 [1, 5, 3, 4, 6, 2],
 [2, 4, 1, 6, 4, 3]]
'''

ans = []
i = 0
done = False # while loop break용 변수 선언
while True:

    if done:
        break

    copy_ = []
    for j in range(N):
        copy_.append(dice[j][:]) # 깊은 복사 시도 (왜? 주사위 눈 값 중 윗면, 아랫면 값을 삭제하는 작업을 반복하기 위해)

    for j in range(N):
        num1 = cmps[i][j]
        num2 = copy_[j][dict_[copy_[j].index(cmps[i][j])]]
        # 인덱스보다 값 자체를 기준으로 지우는 것이 안전할 것 같음
        copy_[j].remove(num1)
        copy_[j].remove(num2)

    # 윗면, 아랫면 값 삭제된 주사위 N개의 눈 값
    ans.append(copy_)

    if i == 4:
        done = True
        break

    i += 1

sums = []
for i in range(5):
    sum = 0
    for j in range(N):
        sum += max(ans[i][j])
    sums.append(sum)

print(max(sums))