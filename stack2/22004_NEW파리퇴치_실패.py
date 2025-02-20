import sys;sys.stdin=open('22004_input.txt')

t=int(input())
for x in range(1,t+1):
    n,h,w = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    max_count = 0

    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]

    r,c = 1,1
    while r < n-1:

        a = h
        b = w
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n:
                count += arr[nr][nc]
        if count > max_count:
            max_count = count
        c += 1
        count = 0
        if c > n-2:
            c = 1
            r += 1

    print(f'#{x}', max_count)
            



