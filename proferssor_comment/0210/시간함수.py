# 명령문 하나의 실행시간의 단위시간 1
# n에 대한 시간함수 -> 명령문의 실행 횟수
'''
def func(n):
    명령문 --> 1번
    for i in range(n):
        명령문 --> n번
        for j in range(i,n):
            명령문 --> n*n
            명령문 --> n*n  --> n**2 + n
        명령문 --> n번

f(n) = n**2 + 3n + 1
'''