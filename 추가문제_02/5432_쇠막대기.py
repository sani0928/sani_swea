import sys; sys.stdin = open('5432_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    
    for i in range(len(arr)):
        if arr[i] == '(' and arr[i+1] == ')':
            arr[i] = '.'
            arr[i+1] = '*'

    total_cnt = 0
    bong_cnt = 0

    for j in range(len(arr)):
        if arr[j] == '(':
            bong_cnt += 1
            total_cnt += 1
        elif arr[j] == ')':
            bong_cnt -= 1
        elif arr[j] == '*':
            total_cnt += bong_cnt


    print('#{} {}'.format(tc,total_cnt))