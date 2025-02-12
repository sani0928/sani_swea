# import sys; sys.stdin = open('12393input.txt')
# str1 글자수를 범위로 지정해서 str2에 1씩 옮겨가며 비교
# 옮겨가며 비교하다 겹치면 1, 끝까지 가도 없으면 0
# str2[0:3] .. str2[1:4] .. str2[2:5] .. str2[6:9]
# t = int(input())

# def Str_Comparison(str1,str2):

#     for i in range(len(str2)-len(str1)):
#         if str1 == str2[i:i+len(str1)]:
#             return f'#{x} 1'
    
#     return f'#{x} 0'

# for x in range(1, t+1):
#     print(Str_Comparison(input(),input()))
# str1 = aaaaaaaaaa 10
# str2 = sfjvdfgnljnglaoshfdgjrieogjaaaaaaaaaa 37
t = 1

# def Str_Comparison(str1,str2):

#     for i in range((len(str2)-len(str1))+1):
#         if str1 == str2[i:i+len(str1)]:
#             return f'#{x} 1'

#     return f'#{x} 0'
    
# for x in range(1, t+1):
#     print(Str_Comparison('aaaaaaaaaa','sfjvdfgnljnglaoshfdgjrieogjaaaaaaaaaa'))


# t = int(input())

# for x in range(1, t+1):
#     str1,str2 = input()

#     for i in range(len(str2)-len(str1)):
#         if str1 == str2[i:i+len(str1)]:
#             print(f'#{x}', 1)
#             break
#         else:
#             print(f'#{x}', 0)
import sys; sys.stdin = open('12393input.txt')  

def Str_Comparison(str1,str2):

    for i in range((len(str2)-len(str1))+1):
        if str1 == str2[i:i+len(str1)]:
            return f'#{x} 1'

    return f'#{x} 0'

t = int(input())
for x in range(1, t+1):
    str1 = input()
    str2 = input()
    print(Str_Comparison(str1,str2))