import sys;sys.stdin=open('16268_input.txt')

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_cnt = 0

    for r in range(n):
        for c in range(m):
            cnt = 0
            cnt += arr[r][c]
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<n and 0<=nc<m:
                    cnt += arr[nr][nc]
            if max_cnt < cnt:
                max_cnt = cnt

    print('#{} {}'.format(x,max_cnt))