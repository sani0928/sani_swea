import sys; sys.stdin = open('1234_input.txt')

def password(pw):

    s = []

    for i in pw:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)

    return s

for x in range(1, 11):
    n,arr = list(input().split())
    print(f'#{x}', ''.join(password(arr)))