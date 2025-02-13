import sys; sys.stdin = open('12396_input.txt')


# str = "print('{} {}'.format(1, 2))'"
# s=[]
# for char in str:
#     s.append(char)
# print(s)

def rhkfghfmfckwwk(str_input):

    s = []

    for rmfwk in str_input:
        if '{' == rmfwk: # 열린 괄호 나오면 스택에 저장
            s.append(rmfwk)
        elif '(' == rmfwk:
            s.append(rmfwk)

        elif '}' == rmfwk:
            if not s: # 열린 괄호 전에 닫힌 괄호가 먼저 나오면 무조건 0
                return 0
            if s[-1] == '{':
                 s.pop()
            else:
                 return 0       
        elif ')' == rmfwk:
            if not s:
                return 0
            if s[-1] == '(':
                 s.pop()
            else:
                 return 0  

    if len(s) != 0: # 정상적인 문장이라면 스택이 비어있어야 함
        return 0
        
    return 1

t = int(input())
for x in range(1, t+1):
    str_input = input().strip()
    print(f'#{x}', rhkfghfmfckwwk(str_input))


# ['(', '(', ')', ')',], ['{', '{', '}', '}']
# {(}) : 교차 조건을 포함
# ()
# print('#{} {}'.format(tc, find))(
# N, M = map(int, input().split()) 


def rhkfghfmfckwwk(str_input):

    s = []
    for char in str_input:
    
        if '{' in char:
            s.append(char)

        elif '}' in char:
                if not s:
                     return 0
                if s[-1] == '{':
                     s.pop()
                else:
                     return 0
    
        elif '(' in char:
            s.append(char)

        elif ')' in char:
                if not s:
                     return 0
                if s[-1] == '(':
                     s.pop()
                else:
                     return 0
    
    if len(s) == 0:
         return 1
    else:
         return 0

t = int(input())
for x in range(1, t+1):
    str_input = input().strip()
    print(f'#{x}', rhkfghfmfckwwk(str_input))