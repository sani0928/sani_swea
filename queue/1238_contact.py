import sys;sys.stdin=open('1238_input.txt')

t = 10
for x in range(1,t+1):
    n, s = map(int,input().split())
    arr = list(map(int,input().split()))
    node = []
    for i in arr:
        if i not in node:
            node.append(i)
    node_count = len(node)
    print(node_count)
    print(len(arr))
    
