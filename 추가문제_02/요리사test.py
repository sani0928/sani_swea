import sys;sys.stdin=open('4012_input.txt')
from itertools import combinations

def aa(matrix):
    global total_min,reset_matrix

    for i in range(n):
        for j in range(i):
            reset_matrix = matrix
            s = matrix[i][j] + matrix[j][i]

            for k in range(n):
                if matrix[i][k] != matrix[i][j]:
                    matrix[i][k] = 0
            
            for l in range(n):
                if matrix[l][i] != matrix[j][i]:
                    matrix[l][i] = 0
            
            for h in matrix:
                print(*h)
            
            lst = []
            for a in range(n):
                for b in range(a):
                    if matrix[a][b] != 0 and matrix[b][a] != 0:
                        if matrix[a][b] + matrix[b][a] != s:
                            lst.append(matrix[a][b] + matrix[b][a])
            min_val = 9999                
            for k in lst:
                c = abs(s - k)
                if min_val > c:
                    min_val = c
                total_min.append(min_val)
            print(total_min)
        
        if i > n:
            return total_min
        

            

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    reset_matrix = matrix

    total_min = []

    print(aa(matrix))

    
    # print(total_min)
'''
00 37 26 52 77 20
32 00 00 00 00 00
54 00 00 79 37 90
92 00 66 00 92 3
64 00 89 89 00 21
80 00 94 68 5 00
'''

    # print(list(set(lst)))
    # lst2 = []
    # min_val = 9999
    # for k in range(int(len(lst)/2)):
    #     s = abs(lst[k] - lst[0-k-1])
    #     if min_val > s:
    #         min_val = s
    # print('#{} {}'.format(tc,min_val))

