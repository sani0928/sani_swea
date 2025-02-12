import sys; sys.stdin = open('9386input.txt')

t = int(input())

for x in range(1, t+1):
    n = int(input())
    arr = list(map(int, input()))

    max_counts = 0
    temp = 0
    for i in arr:
        if i == 1:
            temp += 1
            if max_counts < temp:
                max_counts = temp
        else:
            temp = 0
            
    print(f'#{x}', max_counts)

    # 0이 나오면 temp를 0으로 초기화