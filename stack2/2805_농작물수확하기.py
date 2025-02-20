import sys;sys.stdin=open('2805_input.txt')


def aa(arr,r,c,i):
    global count

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    nr = r + dr[i]
    nc = c + dc[i]
    if 0<=nr<n and 0<=nc<n:
        count += arr[nr][nc]
        arr[nr][nc] = 0
        i += 1
        if i > 3:
            i = 0
        return aa(arr,nr,nc,i)
    return count


t=int(input())

for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]

    r,c = n//2, n//2

    count = arr[r][c]
    arr[r][c] = 0

    print(aa(arr,r,c,0))