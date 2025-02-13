arr = [64,25,10,22,11]
n = len(arr)
# 주어진 범위에서 최소값(idx)를 찾아서 첫번째로 옮긴다.

idx = 0
for i in range(idx+1, n):
    if arr[idx] > arr[i]:
        idx = i

arr[0],arr[idx] = arr[idx],arr[0]
print(arr)


idx = 1
for i in range(idx+1, n):
    if arr[idx] > arr[i]:
        idx = i

arr[1],arr[idx] = arr[idx],arr[1]
print(arr)



idx = 2
for i in range(idx+1, n):
    if arr[idx] > arr[i]:
        idx = i

arr[2],arr[idx] = arr[idx],arr[2]
print(arr)



idx = 3
for i in range(idx+1, n):
    if arr[idx] > arr[i]:
        idx = i

arr[3],arr[idx] = arr[idx],arr[3]
print(arr)

'''
.
.
.
.
.
'''

arr = [64,25,10,22,11]
n = len(arr)

min_idx = 0
for i in range(min_idx+1, n):
    if arr[min_idx] < arr[i]:
        min_idx = i
arr[i],arr[min_idx] = arr[min_idx],arr[i]
print(arr)

