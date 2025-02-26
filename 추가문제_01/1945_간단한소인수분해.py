import sys;sys.stdin=open('1945_input.txt')

t = int(input())
for test_case in range(1,t+1):
    N = int(input())
    lst = []
    for i in [2,3,5,7,11]:
        temp_cnt = 0
        while (N/i).is_integer():

            N = N/i
            
            temp_cnt += 1
        
        lst.append(temp_cnt)
        
    print(f'#{test_case}', *lst)


# for i in [2,3,5.5,7,11]:
#     print(isinstance(i,float))

# print(5000/2)