import sys;sys.stdin=open('1979_input.txt')


t = int(input())

for x in range(1,t+1):
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0

    for r in arr:
        
        only1_r = ''.join(str(i) for i in r).split('0')

        for a in only1_r:
            if len(a) == k:
                cnt+=1

    for c in range(n):

        col = [arr[j][c] for j in range(n)]

        only1_c = ''.join(str(l) for l in col).split('0')

        for b in only1_c:
            if len(b) == k:
                cnt+=1

    
    print(f'#{x}', cnt)
