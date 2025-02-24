import sys;sys.stdin=open('11652_input.txt')
from collections import deque

def searching_end(i,j,n):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([i,j])
    visited[i][j] = 1

    while q:
        r,c = q.popleft()
        if arr[r][c] == 3:
            return 1
        for dr,dc in ([0,1],[1,0],[0,-1],[0,-1]):
            nr,nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<n and arr[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append([nr,nc])
                visited[nr][nc] = visited[r][c] + 1
    return 0
            

def searching_start(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i,j

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    fi,fj = searching_start(n)
    result = searching_end(fi,fj,n)
    print(result)