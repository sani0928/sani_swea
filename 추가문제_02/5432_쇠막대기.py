import sys; sys.stdin = open('5432_input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = input()
    iron = []
    count = 0

    for i in range(len(lst)):
        if lst[i] == '(':           # '('인 경우 append
            iron.append('(')
        elif lst[i] == ')':         # ')'인 경우
            if lst[i-1] == '(':     # 경우1. 레이저
                iron.pop()
                count += len(iron)
                print('레이저', count)
            else:                   # 경우2. 쇠막대
                iron.pop()
                count += 1
                print('쇠막대', count)
    
    print(f'#{tc} {count}')