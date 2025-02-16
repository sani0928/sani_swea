import sys;sys.stdin=open('20396_input.txt')

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(m):
        i,j = map(int,input().split())
        for k in range(j): # j를 순차적으로 순회
            if i+k <= len(arr): # 범위 초과하기 전까지만
                arr[i+k-1] = arr[i-1] # i-1~i+j-1 까지 (i-1)번째 값으로 변환

    print(f'#{x}', *arr)