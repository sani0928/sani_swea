import sys; sys.stdin = open('22375_input.txt')

t= int(input())
for x in range(1,t+1):
    n = int(input())
    start_switches = list(map(int,input().split()))
    end_switches = list(map(int,input().split()))
    i = 0 ; cnt = 0
    while start_switches != end_switches:

        if start_switches[i] == end_switches[i]:
            pass
        else:
            cnt += 1
            if start_switches[i] == 0:
                start_switches[i] = 1
            else:
                start_switches[i] = 0

            for j in range(i+1,n):
                if start_switches[j] == 0:
                    start_switches[j] = 1
                else:
                    start_switches[j] = 0
        i += 1

    print(f'#{x}',cnt)


