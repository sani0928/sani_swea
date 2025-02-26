#위에서 아래로
#아래에서 위로
#왼쪽에성 오로
#오른쪽에서 왼으로

#가장 작은 값 선택하고 해당 인덱스 위치는 다음 순서에 고려 x

import sys;sys.stdin=open('11611_input.txt')

t=int(input())
for test_case in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0] * n


    for r in range(n):
        print(min(arr[r][:n]))
