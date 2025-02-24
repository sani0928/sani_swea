import sys; sys.stdin = open('2005_input.txt')

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = [[0]* a for a in range(1,n+1)]

    for b in range(n): # 삼각형 변 1로 감싸기
        arr[b][0] = 1
    for c in range(n):
        arr[c][-1] = 1

    for i in range(1,n): # 안 채우기
        for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{x}')
    for c in arr:
        print(*c)

#
# c = [1,2,3]
# print(c[-1])
#
#
# arr[3][2] = arr[2][1] + arr[2][2]
# arr[3][3] = arr[2][2] + arr[2][3]