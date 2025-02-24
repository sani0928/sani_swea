import sys;sys.stdin=open('1206_input.txt')

for x in range(1,11):
    n = int(input())
    lst = list(map(int,input().split()))
    arr = [[0]*n for _ in range(max(lst))]
    for j in range(n): # ??
        for i in range(0, lst[j]):
            arr[max(lst)-1-i][j] = 1 # 아파트 1로 표시

    cnt = 0
    for r in range(max(lst)):
        for c in range(n):
            # 아파트 층 발견하면 양옆 2칸 이상 뚫려있는 조망권인지 확인하고 카운팅
            if arr[r][c] == 1:
                if arr[r][c+1:c+3] == [0, 0] and arr[r][c-2:c] == [0, 0]:
                    cnt += 1
    
    print(f'#{x}',cnt)


# lst = [0,0,3,3,10,5,0]
# n = len(lst)
# arr = [[0]*n for _ in range(max(lst))]

# for j in range(n): # ??
#     for i in range(0, lst[j]):
#         arr[max(lst)-1-i][j] = 1
# for c in arr:
#     print(*c)

# ss = [1,2,3,4]
# if ss[2:4] == [2,3,4]:
#     print('True')
# else:
#     print('False')