import sys;sys.stdin=open('4012_input.txt')


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    reset = matrix

    # lst : i재료와 j재료와 같이 요리했을 때 발생하니 시너지 모음
    total_min = []
    for i in range(n):
        for j in range(i):
            matrix = [row[:] for row in reset]

            s = matrix[i][j] + matrix[j][i]
            # matrix[1][0] matirx[0][1]

            for a in range(n):
                if matrix[j][a] != matrix[j][i]:
                    matrix[j][a] = 0

            for b in range(n):
                if matrix[i][b] != matrix[i][j]:
                    matrix[i][b] = 0

            for c in range(n):
                if matrix[c][j] != matrix[i][j]:
                    matrix[c][j] = 0

            for d in range(n):
                if matrix[d][i] != matrix[j][i]:
                    matrix[d][i] = 0
            
            # for h in matrix:
            #     print(*h)
            
            lst = []
            for a in range(n):
                for b in range(a):
                    if matrix[a][b] != 0 and matrix[b][a] != 0:
                        if matrix[a][b] + matrix[b][a] != s:
                            lst.append(matrix[a][b] + matrix[b][a])
            # print(lst)
            min_val = 9999                
            for k in lst:
                if min_val > abs(s - k):
                    min_val = abs(s - k)
            total_min.append(min_val)
    print(f'#{tc} {min(total_min)}')

'''
00 37 00 00 00 00
32 00 00 00 00 00
00 00 00 00 37 00
00 00 00 00 00 3
00 00 89 00 00 00
00 00 00 68 00 00
'''

    # print(list(set(lst)))
    # lst2 = []
    # min_val = 9999
    # for k in range(int(len(lst)/2)):
    #     s = abs(lst[k] - lst[0-k-1])
    #     if min_val > s:
    #         min_val = s
    # print('#{} {}'.format(tc,min_val))

