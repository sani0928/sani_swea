import sys; sys.stdin = open('12399_input.txt')
# a = [1, 2, 3, 4]
# b = []
# b.append(a[1:3])
# print(b)


def search(str):
    s = []

    for char in str:
        if s and s[-1] == char:
            s.pop()
        else:
            s.append(char)

    return s

t = int(input())
for x in range(1, t+1):
    str = input()


    print(f'#{x}', len(search(str)))