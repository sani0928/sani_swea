import sys; sys.stdin = open('1954input.txt')



t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    dr = [0, 1, 0, -1] # 오른쪽부터 시작 dr[0],dc[0]는 오른쪽 dr[1],dc[1]는 아래쪽
    dc = [1, 0 , -1, 0]

    r, c = 0, 0
    direction = 0 # 오른쪽으로 이동 시작

    for numbers in range(1, n*n+1): # 총 n*n번 순회

        arr[r][c] = numbers

        nr = r + dr[direction]
        nc = c + dc[direction] # 정해진 방향으로 한 칸씩 이동

        if nc >= n or nr >= n or nc < 0 or nr < 0 or arr[nr][nc] != 0:
            direction = (direction + 1) % 4 # 나머지 계산을 통한 방향전환
            nr = r + dr[direction]
            nc = c + dc[direction]

        r,c = nr, nc
    print(f'#{i}')
    for chunk in arr:
        print(*chunk)
