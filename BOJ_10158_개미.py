w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

'''
1. 일단 우측으로 시간만큼 이동
2. 'w' or 'h'를 벗어난 만큼의 길이는 '2*w' or '2*h'로 나누어 나머지를 구함
3. 왜? 그 '나머지-w' or '나머지-h'의 절댓값만큼 
4. 0 방향으로 이동해야 하기 때문
- 무조건 0 방향으로 고려
- 그래서 초기에 'p' or 'q'에 time값을 모두 더해서 'w' or 'h' 방향으로 이동했고
- 이동한 거리 중 'w' or 'h'의 2배를 나누어줘도 남는 나머지만큼 0 방향으로 이동
'''

if p+time > w:
    p = w-abs(w-(p+time)%(2*w))
else:
    p += time

if q+time > h:
    q = h-abs(h-(q+time)%(2*h))
else:
    q += time

print(p, q)

'''
# 시간 초과
cnt = 0
cnt += time
done = False
while cnt != 0:
    if p < w:
        p += 1
        cnt -= 1
        continue
    elif p == w:
        while p != 0:
            p -= 1
            cnt -= 1
            if cnt == 0:
                done = True
                break
    if done:
        break

cnt += time
done = False
while cnt != 0:
    if q < h:
        q += 1
        cnt -= 1
        continue
    elif q == h:
        while q != 0:
            q -= 1
            cnt -= 1
            if cnt == 0:
                done = True
                break
    if done:
        break

print(p, q)
'''