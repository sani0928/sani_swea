import sys;sys.stdin = open('14555_input.txt')

t = int(input())

for x in range(1, t+1):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '(' and s[i+1] == '|':
            count += 1
        elif s[i] == ')' and s[i-1] == '|':
            count += 1
        elif s[i:i+2] == '()':
            count += 1

    print(f'#{x} {count}')       