import sys;sys.stdin=open('12390_input.txt')
import itertools

t=int(input())
for x in range(1,t+1):
    n,k = map(int,input().split())
    num = [x for x in range(1, 13)]
    count = 0
    for j in itertools.combinations(num,n):
        if sum(j) == k:
            count += 1
    print(f'#{x}', count)
