import sys;sys.stdin=open('11620_input.txt')

def searching_three(r,c):
    if maze[r][c] == 3:
        return True
    
    visited[r][c] = True
    maze[r][c] = 9
    # print('---------')
    # for chunk in maze:
    #     print(*chunk)
    # print('현재좌표({},{})'.format(r,c))

    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0<=nr<n and 0<=nc<n:
            if not visited[nr][nc] and maze[nr][nc] != 1:
                if searching_three(nr,nc):
                    return True
    return False

def searching_start(maze):

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return searching_three(i,j)

t = int(input())
for x in range(1,t+1):
    n = int(input())
    maze = [list(map(int,input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]


    
    result = 1 if searching_start(maze) else 0
    print(f'#{x}', result)
