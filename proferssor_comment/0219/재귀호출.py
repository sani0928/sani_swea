# 재귀 호출도 반복이다.
# 재귀 호출을 통한 반복을 종료하려면 더 이상 재귀호출 안함

def print_hello(i):
    #매개변수를 보고 판단
    if i == 3:
        print('여기가 마지막입니다.')
    else:
        print('hello')
        print_hello(i+1)

print_hello(0)


# 실행순서의 차이
def print_hello(i):
    if i == 3:
        print('여기가 마지막입니다.')
    else:
        # 순서대로 실행
        print_hello(i+1)
        # 역순으로 실행
        print('hello')

print_hello(0)


# 원하는 만큼
arr = [0] * 5
def print_hello(i,n):

    # 매개변수를 보고 판단
    if i == n:
        print(arr)
    else:
        arr[i] = i + 1
        print_hello(i+1,n)
        arr[i] = 0

print_hello(0,5)
print(arr)


cnt = 0
def print_hello(i,n):
    
    # 매개변수를 보고 판단
    if i == n:
        global cnt
        cnt += 1
    else:
        print_hello(i+1,n)
        print_hello(i+1,n) 

print_hello(0,3)
print(cnt) # 2^3