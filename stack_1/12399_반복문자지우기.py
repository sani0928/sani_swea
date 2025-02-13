import sys; sys.stdin = open('12399_input.txt')
# a = [1, 2, 3, 4]
# b = []
# b.append(a[1:3])
# print(b)
11 11

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


ar = '()(((()())(())()))(())'
print(ar.count('('))

'''
닫힌걸 뺀 뒤((()()))()

             
뺀 괄호 보관()()()()()()
()
'''

# 중요한건 조각 갯수 즉, 카운팅을 하는 거
# 쇠막대기의 길이는 짧은 것부터?
# ( 발견시 다음 괄호 탐색
# )라면 레이저 분류, (이라면 계속 진행