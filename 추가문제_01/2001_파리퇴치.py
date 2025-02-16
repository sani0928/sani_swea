import sys;sys.stdin=open('2001_input.txt')

t = int(input())

for x in range(1, t+1):
    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    dr = [0,1,1]
    dc = [1,1,0]
    max_val = 0

    k = m
    for r in range(n):
        for c in range(n):
            temp = 0
            for r2 in range(m):
                for c2 in range(m):
                    if 0<=r+r2<n and 0<=c+c2<n:
                        temp += arr[r+r2][c+c2]
                        if temp > max_val:
                            max_val = temp

    print(f'#{x}',max_val)


