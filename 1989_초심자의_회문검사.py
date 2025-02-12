import sys; sys.stdin = open('1989input.txt')

t = int(input())

'''
for x in range(1, t+1):
    txt = input()
    n = len(txt)
    counts = 0
    for i in range(n//2):       
        if txt[i] == txt[n-1-i]:
            counts += 1
            
    if counts == n//2:
        print(f'#{x}', 1)
    else:
        print(f'#{x}', 0)
'''


for x in range(1, t+1):
    txt = input()
    n = len(txt)
    counts = 0
    for i in range(n//2):       
        if txt[i] != txt[n-1-i]:
            flag = False
            break
        else:
            print('회문입니다.')

# for x in range(1, t+1):
#     txt = input()
#     n = len(txt)
#     counts = 0
#     for i in range(n//2):       
#         if txt[i] != txt[n-1-i]:
#             break
#     else:
#         print('회문입니다.')
print(txt)
