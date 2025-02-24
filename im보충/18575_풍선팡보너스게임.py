import sys
sys.stdin=open('18575_input.txt')

t = int(input())
for x in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
   
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    position = 0
    total_cnt = []
    max_cnt = 0
    min_cnt = arr[0][0]
    position = 0

    while position < n*n:
        for r in range(n):
            for c in range(n):
                position += 1
                cnt = 0
                cnt += arr[r][c]

                for i in range(1,n+1):
                    for j in range(4):
                        nr = r + dr[j]*i
                        nc = c + dc[j]*i
                        if 0<= nr <n and 0<=nc <n:                      
                            cnt += arr[nr][nc]
                total_cnt.append(cnt)
                if max_cnt < cnt:
                    max_cnt = cnt
                    
    print(f'#{x}', max_cnt - min(total_cnt))
                        


    

