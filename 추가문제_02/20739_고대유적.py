import sys; sys.stdin = open('20739_input.txt')


t = int(input())
for x in range(1, t+1):
    n,m = list(input().split())
    arr = list(map(int, input().split()))
for c in arr:
    print(c)
   
    total_count = 0

    # 행 순회
    for r in range(n):
        for c in range(m):
            temp_count = 0
            if arr[r][c] == 1:
                temp_count += 1
                if temp_count >= 2:
                    total_count += 1
        print(total_count)