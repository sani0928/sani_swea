import sys; sys.stdin = open('1210input.txt')
'''
1. 열우선으로 순회하면서 내려감
2. 양 옆 행에 1이 있다면 행우선으로 전환
3. 아래 열에 1이 있다면 열우선으로 전환
4. 반복
'''
n=100

t = int(input())
arr = [list(map(int,input().split())) for _ in range(100)]


# for chunk in arr:
#     print(chunk)

position = 0
    
def start(lst):
    global position
    for c in range(n):
        for r in range(position, n):
            arr[r][c]
            position += 1
            return position
    
        if lst[r][c-1] or lst[r][c+1] == 1:
            change(lst)

def change(lst):
    global position
    for r in range(position, n):
        for c in range(n):
            lst[r][c]
    
    
        if lst[r+1][c] == 1:
            start(lst)


print(start(arr))