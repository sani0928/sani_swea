import sys;sys.stdin=open('11151_input.txt')
t=int(input())
for x in range(1, t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    sum_lst = []
    for i in range(len(arr)-1):
        sum_lst.append(arr[i] + arr[i+1])

    max_val = sum_lst[0]
    for j in range(len(sum_lst)):
        if sum_lst[j] > max_val:
            max_val = sum_lst[j]
    
    print(f'#{x}', max_val)