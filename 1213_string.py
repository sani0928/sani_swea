import sys; sys.stdin = open('1213input.txt', encoding='utf-8')

def string(str, s):
    count = 0
    i = 0

    for _ in range(10):
        while i <= (len(str) - len(s)):

            if str[i:i+len(s)] == s:
                count += 1
                i += len(s)
            else:
                i += 1

    return count

for x in range(1, 11):
    t = int(input())
    s = input()
    str = input()

    print(f'#{x}', string(str, s))
