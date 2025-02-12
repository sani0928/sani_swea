n = int(input())


arr = [[0] * n for _ in range(n)]

# 왼쪽 -> 아래 -> 오른쪽 -> 위 (반시계방향)
dr = [0,1,0,-1]
dc = [-1,0,1,0]

r = 1
c = 1

direction = 0

for num in range(1, n*n+1):

    arr[r][c] = num

    # 오른쪽으로 이동 시작
    nr = r + dr[direction]
    nc = c + dc[direction]

    if nc < 0 or nr >= n or nc >= n or nr < 0 or arr[nr][nc] != 0:
        direction = (direction+1)%4
        nr = r + dr[direction]
        nc = c + dc[direction]

    r,c = nr,nc
    
for i in arr:
    print(*i)