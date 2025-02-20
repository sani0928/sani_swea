import sys;sys.stdin=open('2805_input.txt')


def aa(arr,dr,dc,r,c):
    global count

    while True:
        moved = False

        for i in range(4):
            nr = r +dr[i]
            nc = c +dc[i]
            if 0<=nr<n and 0<=nc<n:
                if arr[nr][nc] > 0:
                    count += arr[nr][nc] # 땅의 수익만큼 카운팅
                    arr[nr][nc] = 0 
                    r,c = nr,nc
                    aa(arr,dr,dc,nr,nc)
                    moved =True
                    break
            
        if not moved:
            break

t=int(input())
for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    r,c = n//2, n//2
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    count=0
    result = aa(arr,dr,dc,r,c)
    print(result)