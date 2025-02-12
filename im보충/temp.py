# n = 돌의 수, m = 시행 횟수, i = 기준돌, j = 마주보는 돌의 갯수

import sys; sys.stdin = open('20397input.txt')

def swing_stone(n,center,j,stone):

    center -= 1
    # j += 1 # range 특성상 값의 -1까지 반복하기 때문에
    for spread in range(1,j+1):
        # center = j = 2 # stone[center-j] = a[0], stone[center+j] = a[2]
        if center-spread < 0 or center+spread >= n:
            break

        if stone[center-spread] == stone[center+spread]:            
            if stone[center-spread] == 0:
                stone[center-spread] = stone[center+spread] = 1
            else: #stone[center-j] == 1
                stone[center-spread] = stone[center+spread] = 0
        else: # stone[center-j] != stone[center+j]
            pass
    return stone
    
t = int(input())
for x in range(1, t+1):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        i,j = map(int, input().split())

    #     result = swing_stone(n,i,j,arr)
    # print(f'#{x}', *result)

    #     swing_stone(n,i,j,arr)
    # print(f'#{x}', *swing_stone(n,i,j,arr))
        
    # print(f'#{x}', *swing_stone(n,i,j,arr))