import sys;sys.stdin=open('11012_input.txt')

t=int(input())
for x in range(1,t+1):
    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    total_sum = 0

    for _ in range(m):
        start_r, start_c, length = map(int,input().split())

        for r in range(length):
            for c in range(length):
                if 0<=start_r+r<n and 0<=start_c+c<n: # 범위 내에서만
                    total_sum += arr[start_r+r][start_c+c] # 행우선 순회하면 덧셈
                    arr[start_r+r][start_c+c] = 0 # 겹쳐지는 부분 중복 방지를 위해 지나간 위치는 0으로 처리
    print(f'#{x}',total_sum)

