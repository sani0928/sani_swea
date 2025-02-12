import sys; sys.stdin = open('3143input.txt')

# A는 최종적으로 써야 하는 문자열
# B에 주어진 문자열이 A와 중복된다면 카운팅하고 중복 제거
# 이후 남은 문자열 계산

t = int(input())
for x in range(1, t+1):
    a,b =input().split()
    count = 0
    i = 0
    
    while i <= (len(a) - len(b)):
    
        if b == a[i:i+len(b)]:
            count += 1
            i += len(b)
        else:
            i += 1
    calculate = count + (len(a)-(count*len(b)))
    print(f'#{x}', calculate)