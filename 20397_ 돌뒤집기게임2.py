import sys; sys.stdin = open('20397_input.txt')

t=int(input())
for x in range(1,t+1):
    n,m = map(int,input().split())
    stones = list(map(int,input().split()))
    for _ in range(m):
        i,j = map(int,input().split())
        i -= 1
        for k in range(1,j+1):
            if i+k<n and 0<=i-k:
                if stones[i+k] != stones[i-k]:
                    pass
                else:
                    if stones[i+k] == 0:
                        stones[i+k],stones[i-k] = 1,1
                    else:
                        stones[i+k],stones[i-k] = 0,0
            else:
                break

    print(f'#{x}', *stones)




