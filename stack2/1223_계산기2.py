import sys;sys.stdin=open('1223_input.txt')

# def result(num,stack):

#     operators = ('+','*')

#     for i in range(len(num)):
#         if num[i].isdigit():

#             stack.append(num[i])
#         elif num[i] in operators:
#             if len(stack) >= 2:
#                 if num[i] == '+':
#                     b = int(stack.pop())
#                     a = int(stack.pop())
#                     stack.append(a+b)
#                 elif num[i] == '*':
#                     b = int(stack.pop())
#                     a = int(stack.pop())
#                     stack.append(a*b)

#                 else:
#                     continue
            

t = 10
for test_case in range(1, t+1):
    n = int(input())
    n_list = list(input())
 
    stack = []
    num = []
    operators = ('+','*')
 
    for i in range(n):
        if n_list[i].isdigit():
            num.append(n_list[i])
        elif n_list[i] == '+':
            while stack:
                num.append(stack.pop())
            stack.append(n_list[i])
        elif n_list[i] == '*':
            while stack and stack[-1] == '*':
                num.append(stack.pop())
            stack.append(n_list[i])
 
    while stack:
        num.append(stack.pop())

    for i in range(len(num)):
        if num[i].isdigit():

            stack.append(num[i])
        elif num[i] in operators:
            if len(stack) >= 2:
                if num[i] == '+':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a+b)
                elif num[i] == '*':
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a*b)

                else:
                    continue

    print('#{} {}'.format(test_case,*stack))