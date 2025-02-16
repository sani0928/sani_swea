import sys;sys.stdin=open('5356_input.txt')

t = int(input())
for x in range(1, t+1):
    arr = [input() for _ in range(5)]
    reading = []
    max_idx = 0
    for i in range(5):
        if len(arr[i]) > max_idx:
            max_idx = len(arr[i])

    for c in range(max_idx):
        for r in range(5):
            if c < len(arr[r]):
                reading.append(arr[r][c])

    print(f'#{x}', ''.join(reading))
