import sys; sys.stdin = open('20739_input.txt')

t = int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    # 행우선
    temp_r = []
    for r in range(n):
        count = 0
        for c in range(m):
            if arr[r][c] == 1:
                count += 1
        temp_r.append(count)
    if count == 0:
        temp_r = 0
    
    # print(f'#{x} 행우선',temp_r)

    # 열우선
    temp_c = []
    for c in range(m):
        count = 0
        for r in range(n):
            if arr[r][c] == 1:
                count += 1
        temp_c.append(count)
    if count == 0:
        temp_c = 0
    
    # print(f'#{x} 열우선',temp_c)

    # 대각선
    temp_x = []
    for c in range(m):
        count = 0
        for r in range(n):
            if arr[r][c] == 1:
                count += 1
        temp_x.append(count)

    print(f'#{x} 대각선',temp_x)

    print(f'#{x}',max(max(temp_r), max(temp_c)))


