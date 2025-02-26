import sys;sys.stdin=open('2805_input.txt')




t=int(input())

for x in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input())) for _ in range(n)]

    center = n//2
    val = center

    result = 0
    for r in range(n):
        for c in range(n):
            if abs(r-center) + abs(c-center) <= val:
                result += matrix[r][c]

    print('#{} {}'.format(x,result))