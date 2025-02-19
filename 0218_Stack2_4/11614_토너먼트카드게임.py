import sys;sys.stdin=open('11614_input.txt')

# 1가위 2바위 3보 / 무승부면 작은 반호가 승자

def find_min(start, end):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    left = find_min(start, mid)
    right = find_min(mid+1, end)

    if left < right:
        return left
    return right

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    print(find_min(0, len(arr)-1))