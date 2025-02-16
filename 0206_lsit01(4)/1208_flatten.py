import sys;sys.stdin=open('1208_input.txt')


t = 10
for x in range(1,t+1):
    
    n = int(input())
    boxs = list(map(int, input().split()))
    
    for _ in range(n):

        min_val = boxs[0]
        max_val = boxs[0]
        min_idx = 0
        max_idx = 0

        for i in range(len(boxs)):
            if boxs[i] < min_val:
                min_val = boxs[i]
                min_idx = i

        for j in range(len(boxs)):                
            if boxs[j] > max_val:
                max_val = boxs[j]
                max_idx = j

        boxs[max_idx] -= 1
        boxs[min_idx] += 1
    print(boxs)
    print(f'#{x}', max(boxs) - min(boxs))
