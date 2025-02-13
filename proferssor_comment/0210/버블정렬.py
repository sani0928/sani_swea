# 버블정렬
# - 인접한 두 원소를 비교해 앞이 크면 교환 (총 n-1번)
# 앞 원소의 인덱스 i를 생성하고 뒷 원소 인덱스 i+1를 비교
# 그러므로 i는 0부터 n-2까지
arr=[64,25,10,22,11]
n = len(arr)


for i in range(0, n-1):    
    for j in range(0, n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
            print(arr)


# for i in range(n-1, 0, -1):    
#     for j in range(0, i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1],arr[j]
#             print(arr)

