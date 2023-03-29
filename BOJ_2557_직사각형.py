for _ in range(4):
    lst = list(map(int, input().split()))
    minX = min(lst[0], lst[2], lst[4], lst[6]) # 첫번째로 입력된 직사각형의 좌측 x 좌표
    maxX = max(lst[0], lst[2], lst[4], lst[6]) # 첫번째로 입력된 직사각형의 우측 x 좌표
    minY = min(lst[1], lst[3], lst[5], lst[7]) # 두번째로 입력된 직사각형의 우측 x 좌표
    maxY = max(lst[1], lst[3], lst[5], lst[7]) # 두번째로 입력된 직사각형의 우측 x 좌표

    ar = lst[2]-lst[0]
    br = lst[6]-lst[4]
    ac = lst[3]-lst[1]
    bc = lst[7]-lst[5]
    allX = ar + br # 두 직사각형의 가로 길이를 온전하게 합한 값 (겹치지 않는다는 가정하에)
    allY = ac + bc # 두 직사각형의 세로 길이를 온전하게 합한 값 (겹치지 않는다는 가정하에)

    if (maxX-minX) < allX and (maxY-minY) < allY:
        print('a')
    elif (maxX-minX) == allX and (maxY-minY) < allY or (maxY-minY) == allY and (maxX-minX) < allX:
        print('b')
    elif (maxX-minX) == allX and (maxY-minY) == allY:
        print('c')
    else:
        print('d')