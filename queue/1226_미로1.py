import sys;sys.stdin=open('1226_input.txt')

def searching_three(r,c):
    if maze[r][c] == 3:
        return True
    
    visited[r][c] = True
    # maze[r][c] = 9
    # print('---------')
    # for chunk in maze:
    #     print(*chunk)
    # print('현재좌표({},{})'.format(r,c))

    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0<=nr<16 and 0<=nc<16:
            if not visited[nr][nc] and maze[nr][nc] != 1:
                if searching_three(nr,nc):
                    return True
                
    return False

for x in range(1,11):
    n=int(input())
    maze = [list(map(int,input().strip())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    result = 1 if searching_three(1,1) else 0
    # if x == 2:
    #     result = 1
    print(f'#{x}', result)
