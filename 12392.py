# arr = [64, 25, 10, 22, 11]
# N = len(arr)
# # 0 ~ N-1 에서 최소값 찾기
# # idx = 0
# # for j in range(1, N):
# #     if arr[idx] > arr[j]:
# #         idx = j
# # arr[0], arr[idx] = arr[idx], arr[0]
# # print(arr)
# #
# # # 1 -> N-1에서 최소값 찾기
# # idx = 1
# # for j in range(2, N):
# #     if arr[idx] > arr[j]:
# #         idx = j
# # arr[1], arr[idx] = arr[idx], arr[1]
# # print(arr)

# for i in range(4):
#     # i: 범위 시작, 최소값의 저장 위치
#     idx = i
#     for j in range(i+1, N):
#         if arr[idx] > arr[j]:
#             idx = j
#     arr[i], arr[idx] = arr[idx], arr[i]
#     print(arr)

import sys; sys.stdin = open('12392input.txt')
t = int(input())
for x in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = []

    for i in range(n):

        if i % 2 == 0: # 홀수일 땐 최대값
            idx = 0
            for j in range(1, len(arr)):
                if arr[idx] < arr[j]:
                    idx = j
        
        else: # 짝수일 땐 최소값
            idx = 0
            for j in range(1, len(arr)):
                if arr[idx] > arr[j]:
                    idx = j
        new_arr.append(arr[idx]) # 반복하며 찾은 최대값과 최소값을 저장
        arr.pop(idx) #저장한 값은 arr에서 제거
    print(f'#{x}', *new_arr[:10])
