import sys; sys.stdin = open('16242input.txt')

t = int(input())

for x in range(1, t+1):
    r1,c1,n,m=map(int,input().split())
    
    arr = [[0] * 10 for _ in range(10)]
    for i in range(0, n*m):
        num = 1
        for r in range(r1, r1+m):
            if (r-r1) % 2 == 0: # 무조건 시작은 왼쪽에서 오른쪽으로 순회
                for c in range(c1, c1+n):
                    arr[r][c] = num
                    num += 1
            else:
                for c in range(c1+n-1, c1-1, -1): # 역순으로 순회 
                    arr[r][c] = num
                    num += 1
    
    
    print(f'#{x}')
    for chunk in arr:
        print(*chunk)