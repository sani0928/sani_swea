import sys; sys.stdin = open('1979input.txt')

# r행과 c열 순회하면서 '1'이 k번 연속되면 카운팅
# * k번이 초과되면 카운팅 x

t = int(input())

for x in range(1,t+1):
    n, k = map(int, input().split())
    
    arr = []
    total_counts = 0
    for j in range(n):
        
        lst = list(map(int, input().split()))
        arr.append(lst)
    
    # 가로로 순회
    for r in range(n):
        temp_counts = 0
        for c in range(n):
            if arr[r][c] == 1:
                temp_counts += 1
            if arr[r][c] == 0 or c == n-1:
                if temp_counts == k:
                    total_counts += 1
                temp_counts = 0
    # 세로로 순회
    for c in range(n):
        temp_counts = 0
        for r in range(n):
            if arr[r][c] == 1:
                temp_counts += 1
            if arr[r][c] == 0 or r == n-1:
                if temp_counts == k:
                    total_counts += 1
                temp_counts = 0
        
    print(f'#{x}', total_counts)