T = int(input())

for test_case in range(1, T+1):

    money = int(input())

    store = {50000: 0 , 10000: 0 , 5000: 0 , 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    for i in range(8):
        while money - list(store.keys())[i] >= 0:
            money -= list(store.keys())[i]
            store[list(store.keys())[i]] += 1

    print(f'#{test_case}')
    print(*store.values())