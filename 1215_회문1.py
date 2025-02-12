import sys; sys.stdin = open('1215input.txt')

for x in range(1, 11):
    n = int(input())
    arr = [input() for _ in range(8)]
    count = 0

    # 가로로 순회
    for r in range(8):
        for c in range(8-n+1):
            slicing_r = arr[r][c:c+n]
            if slicing_r == slicing_r[::-1]:
                count += 1
    
    # 세로로 순회
    for r in range(8):
        reverse_arr = [arr[c][r] for c in range(8)]
        for c in range(8-n+1):
            if reverse_arr[c:c+n] == reverse_arr[c:c+n][::-1]:
               count += 1

    print(f'#{x}', count)

