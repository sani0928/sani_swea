import sys; sys.stdin = open('1218_input.txt')

rhkfgh_zip = '({[<)}]>'

def a(input_str):

    s = []

    for char in input_str:
        if rhkfgh_zip[0] in char:
            s.append(char)
        elif rhkfgh_zip[1] in char:
            s.append(char)
        elif rhkfgh_zip[2] in char:
            s.append(char)
        elif rhkfgh_zip[3] in char:
            s.append(char)

        if rhkfgh_zip[4] in char:
            if not s:
                return 0
            if s[-1] == rhkfgh_zip[0]:
                s.pop()
            else:
                return 0
        
        elif rhkfgh_zip[5] in char:
            if not s:
                return 0
            if s[-1] == rhkfgh_zip[1]:
                s.pop()
            else:
                return 0
            
        elif rhkfgh_zip[6] in char:
            if not s:
                return 0
            if s[-1] == rhkfgh_zip[2]:
                s.pop()
            else:
                return 0
        
        elif rhkfgh_zip[7] in char:
            if not s:
                return 0
            if s[-1] == rhkfgh_zip[3]:
                s.pop()
            else:
                return 0
            
    if len(s) == 0:
        return 1
    else:
        return 0

t = 10
for x in range(1, t+1):
    n = int(input())
    input_str = input().strip()
    print(f'#{x}',a(input_str))