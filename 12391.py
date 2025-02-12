import sys; sys.stdin = open('12391input.txt')

t = int(input())

def Searching(p, key):
    l, r = 1, p
    times = 0

    while l <= r:
        times += 1
        mid = (l + r)//2

        if mid == key:
            return times
        elif mid > key:
            r = mid
        else:
            l = mid

for x in range(1, t+1):
    p, pa, pb = map(int,input().split())

    A = Searching(p, pa)
    B = Searching(p, pb)

    if A < B:
        output = 'A'
    elif A > B:
        output = 'B'
    else:
        output = 0

    print(f'#{x}', output)