import sys; sys.stdin = open('11573_input.txt')

def a(arr):

    s = []
    total_sum = 0

    for i in arr:
        if i == 0:
            s.pop()
        else:
            s.append(i)
    
    for j in s:
        total_sum += j
    
    return total_sum

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{x}',a(arr))