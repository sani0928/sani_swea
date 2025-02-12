# n = 돌의 수, m = 시행 횟수, i = 기준돌, j = 마주보는 돌의 갯수

import sys; sys.stdin = open('20397input.txt')

t = int(input())
for x in range(1, t+1):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        i,j = map(int, input().split())

        i -= 1
        # j += 1 # range 특성상 값의 -1까지 반복하기 때문에
        for z in range(1,j+1):
            # i = j = 2 # arr[i-j] = a[0], arr[i+j] = a[2]
            if i-z < 0 or i+z >= n:
                break
            if arr[i-z] == arr[i+z]:    
                if arr[i-z] == 0:
                    arr[i-z] = arr[i+z] = 1
                else: #arr[i-j] == 1
                    arr[i-z] = arr[i+z] = 0

            else: # arr[i-j] != arr[i+j]
                pass
        
    print(*arr)
'''
범위 초과 했을 때 즉, i-j < len(arr) - n 혹은 i + j > len(arr)
어떻게 할 것인가
'''

# arr = ['0','1','2','3','4']
# arr[0] = arr[1] = '5'
# print(arr)