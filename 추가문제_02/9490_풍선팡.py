import sys; sys.stdin = open('9490_input.txt')

t = int(input())
for x in range(1, t+1):
    n,m = map(int, input().split())
    arr = [input().split() for _ in range(n)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    count = 0
    max_val = 0

    for r in range(n):
        for c in range(n):
            if arr[r][c] >= 1:
                arr[r][c] -= 1
                count += 1
                for i in range(4):
                    if arr[r+dr[i]][c+dr[i]] >= 1:
                        arr[r+dr[i]][c+dr[i]] -= 1
                        count += 1