'''
0~9까지 임의의 카드 3장을 뽑아서 연속된 숫자 3장이면 run, 동일한 숫자 3장이면 triplet
run 혹은 triplet이 한번에 2번 나오면 baby-gin
'''

# arr  = [2, 3 ,7]
# for i1 in range(3):
#     for i2 in range(3):
#         if i1 != i2:
#             for i3 in range(3):
#                 if i1 != i3 and i2 != i3:
#                     print(arr[i1], arr[i2], arr[i3])

num = int(input())
c = [0] * 12 # c[10]과 c[11]은 항상 0과 run 확인을 위한 여분

for _ in range(6): # 6번 반복
    c[num%10] += 1 # num%10의 1의 자리
    num //= 10 # num의 1의 자리

print(c)