import sys
sys.stdin=open('18575_input.txt')

t = int(input())
for x in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for c in arr:
        print(c)

    count = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    k = n
    for c in range(n):
        for i in range(1,k):
            nc = c + dc[0]*k
            if 0<=nc<n:
                arr[0][nc] -= 1


    for c in arr:
        print(*c)
    print(count)
