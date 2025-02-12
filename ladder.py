import sys; sys.stdin = open('ladder.txt')
arr = []
n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for line in arr:
    print(*line)

r = c = 0
for i in range(n): # 처음 2자리를 찾는 중
    if arr[n - 1][i] == 2:
        r, c, = n - 1, i
        break

while r != 0:
    # 왼쪽과 오른쪽에 길이 있냐
    if c-1 >= 0 and arr[r][c-1] == 1: # a and b : a가 false면 b는 실행 x
        c -= 1
    elif c < n-1 and arr[r][c+1] == 1:
        c += 1
    else: # 없다면 위로 가자
        r -= 1