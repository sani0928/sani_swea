import sys; sys.stdin = open('20739_input.txt')

t = int(input())
for test_case in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    max_cnt = 0
    #행
    for r in range(n):
        for c in range(m):
            cnt = 0
            if arr[r][c] == 1:
                dc = 0

                while c+dc<m and arr[r][c+dc] == 1:
                    dc += 1
                    cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
    #열
    for c in range(m):
        for r in range(n):
            cnt = 0
            if arr[r][c] == 1:
                dr = 0

                while r+dr<n and arr[r+dr][c] == 1:
                    dr += 1
                    cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
            if max_cnt < 2:
                max_cnt = 0

    print('#{} {}'.format(test_case, max_cnt))


