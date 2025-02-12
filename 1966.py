import sys; sys.stdin = open('1966input.txt')

t = int(input())
for x in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result =[]
    for i in range(len(arr)):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(f'#{x}', *arr)