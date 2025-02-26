import sys;sys.stdin=open('2805_input.txt')




t=int(input())

for x in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]

    r,c = n//2, n//2