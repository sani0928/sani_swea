import sys;sys.stdin=open('1223_input.txt')

for x in range(10):
    n = int(input())
    arr=[*map(lambda x:int(x) if x.isdigit() else x, input())]
    print(arr)
                