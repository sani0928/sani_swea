import sys;sys.stdin=open('1222_input.txt')

for x in range(1, 11):
    n = int(input())
    arr = list(input().strip())
    onlyint = []
    for i in range(n):
        # if not '+' in arr[i]:
        if arr[i].isdigit() == True:
            onlyint.append(arr[i])

    onlyint = list(map(int,onlyint))

    cnt = 0
    for j in onlyint:
        cnt += j
    
    print('#{} {}'.format(x,cnt))

