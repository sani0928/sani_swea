import sys;sys.stdin=open('1225_input.txt')

from collections import deque

t = 10
for x in range(1,t+1):
    n = int(input())
    q = deque(map(int,input().split()))
    i = 1
    while q[-1] > 0:

        if i > 5:
            i = 1

        q.append(q.popleft()-i)

        i += 1
        
    q[-1] = 0
    print(f'#{x}', *q)