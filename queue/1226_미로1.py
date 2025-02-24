import sys;sys.stdin=open('1226_input.txt')
from collections import deque

def searching_end(fi,fj):
    visited = [[0]*16 for _ in range(16)]
    q = deque()
    q.append([fi,fj])
    visited[fi][fj] = 1

    while q:
        r,c = q.popleft()
        if r == 11 and c == 11:
            return 1
        for dr,dc in ([0,1],[1,0],[0,-1],[0,-1]):
            nr,nc = r + dr, c + dc
            if 0<=nr<16 and 0<=nc<16 and arr[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append([nr,nc])
                visited[nr][nc] = visited[r][c] + 1
    return 0

def searching_start():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i,j

t = 10
for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    fi,fj = print(searching_start())
    result = searching_end(fi,fj)
    print(result)