def msort(s, e):
    if s == e: # 시작 인덱스와 종료 인덱스가 같다면 (한 칸이라면) 종료
        return
    else:
        m = (s+e)//2
        msort(s, m)
        msort(m+1, e)
        # merge()
        k = 0
        l, r = s, m+1 # 왼쪽과 오른쪽 파트에서 각각 가장 작은 숫자 위치
        while l <= m or r <= e:
            if l <= m and r <= e:
                if arr[l] <= arr[r]:
                    tmp[k] = arr[l] # 더 작은 원소를 복사
                    l += 1 # 왼쪽 파트 인덱스 한칸 이동
                else:
                    tmp[k] = arr[r] # 더 작은 원소를 복사
                    r += 1 # 오른쪽 파트 인덱스 한칸 이동
                k += 1
            elif l <= m: # 왼쪽 파트만 남아있는 경우
                while l <= m:
                    tmp[k] = arr[l]
                    l += 1
                    k += 1
            elif r <= e: # 오른쪽 파트만 남아있는 경우
                while r <= e:
                    tmp[k] = arr[r]
                    r += 1
                    k += 1
        # tmp를 arr에 복사
        i = 0
        while i < k:
            arr[s+i] = tmp[i]
            i += 1
        return

arr = list(map(int, input().split()))
tmp = [0] * 1000000
msort(0, 1000000-1)
print(arr[500000])