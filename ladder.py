import sys; sys.stdin = open('ladder.txt')


for x in range(1,11):
    n = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    
    dr=[0,0,-1] #왼,오,위
    dc=[1,-1,0]
    r,c = 99,0
    for i in range(100):
        if arr[99][i] == 2:
            c = i
    
    while r > 0:

        for j in range(3):
            nr = r + dr[j]
            nc = c + dc[j]

            if 0<=nr<100 and 0<=nc<100 and arr[nr][nc] == 1:
                arr[r][c] = 0
                r,c= nr,nc
                break
        # s = (r,c)

        # print('현재',s)

    print(f'#{x}', c)
