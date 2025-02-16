# import sys;sys.stdin = open ('12397_input.txt')

small_paper = [[1] * 10 for _ in range(20)]
paper = [[1] * 20 for _ in range(20)]

t = int(input())

for x in range(1,t+1):
    n = int(input())
    panel = [[0] * 20 for _ in range(n)]

    
