#위에서 아래로
#아래에서 위로
#왼쪽에성 오로
#오른쪽에서 왼으로

#가장 작은 값 선택하고 해당 인덱스 위치는 다음 순서에 고려 x

import sys;sys.stdin=open('11611_input.txt')

t=int(input())
for test_case in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    factorial_val = 1
    
    for v in range(1,n+1):
        factorial_val *= v
    r = 0 ; c = 0
    cnt = 0
    min_cnt = 9999
    def sum(r,c):

        c = 0

        while True:

            if visited[r][c] == True:
                for i in range(r):
                    if visited[r-i][c] != True:
                        cnt += matrix[r][c]
                        c+=1
                    else:
            else:
                cnt += matrix[r][c]
            
            sum(r+1,c)
        
    


