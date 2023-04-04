T = int(input())

def find_set(x):
    while x != rep[x]:  # x == rep[x]가 될 때까지
        x = rep[x]
    return x

def union(x, y):  # y의 대표 원소가 x의 대표 원소를 가리키도록
    rep[find_set(y)] = find_set(x)

for tc in range(1, T+1):

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # makeset()
    rep = [i for i in range(n+1)]

    for i in range(m):
        union(data[i*2], data[i*2+1])

    cmp = []
    for i in range(1, n+1):
        cmp.append(find_set(rep[i]))

    print(f'#{tc} {len(set(cmp))}')