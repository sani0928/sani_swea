import sys;sys.stdin=open('11652_input.txt')

def traveral(r,c,dist):

    if maze[r][c] == 3:
        return dist

    visited[r][c] = True

    # maze[r][c] = '*'
    # print('-----')
    # for chunk in maze:
    #     print(*chunk)
    # for chunk2 in visited:
    #     print(*chunk2)
    # print(dist)
    
    min_dist= None

    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0<=nr<n and 0<=nc<n:
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                test = traveral(nr,nc,dist+1)
                if test is not None:
                    if min_dist is None:
                        min_dist = test
                    else:
                        min_dist = min(test,min_dist)
                
    visited[r][c] = False

    return min_dist

t=int(input())
for x in range(1,t+1):
    n=int(input())
    maze = [list(map(int,input().strip())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_r,start_c = i,j
                # print(i,j)
    result = traveral(start_r,start_c,-1)
    if result == None:
        result = 0
    print('#{} {}'.format(x,result))



    

