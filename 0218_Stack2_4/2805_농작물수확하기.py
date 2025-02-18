import sys;sys.stdin=open('2805_input.txt')

t=int(input())
for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    r,c = n//2, n//2
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    while r < n or c < n:
        for i in range(4):
            for j in range(1,n):
                nr = r +dr[i]*j
                nc = c +dc[i]*j
                if 0<=nr<n and 0<=nc<n:
                    arr[nr][nc] = 99 1
    for c in arr:
        print(f'#{x}',*c)