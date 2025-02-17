import sys; sys.stdin = open('9490_input.txt')

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    total_sum = 0

    for r in range(n):
        for c in range(m):
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]
                if 0<=nr<n and 0<=nc<m: