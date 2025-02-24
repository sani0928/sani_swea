import sys; sys.stdin = open('12397_input.txt')


def aa(n):
    dp = [0] * (n+1)
    dp[10] = 1
    dp[20] = 3
    for i in range(30,n+1,10):
        dp[i] = dp[i-10] + 2 * dp[i-20]

    return dp[n]

t = int(input())
for x in range(1,t+1):
    print(f'#{x}', aa(int(input())))