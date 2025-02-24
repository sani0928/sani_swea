import sys;sys.stdin=open('1954_input.txt')

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    r=0;c=0

    i = 0
    for num in range(1, n*n+1):
        arr[r][c] = num
        nr = r + dr[i]
        nc = c + dc[i]

        if nr>=n or nc>=n or arr[nr][nc] != 0:
            i = (i+1)%4
            nr = r + dr[i]
            nc = c + dc[i]
        r,c=nr,nc
        
    print(f'#{x}')
    for c in arr:
        print(*c)