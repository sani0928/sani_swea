import sys; sys.stdin = open('1288_input.txt')

t = int(input())
for x in range(1, t+1):
    n = int(input());k=1;lst = set() # 중복 방지
    while len(lst) < 10: # 중복 없는 리스트, 모든 자릿수가 빠짐 없이 들어가면 길이는 10
        a = k*n # 초기엔 1*n
        lst.update(map(int, str(a))) # 값은 한자리씩 나눠서 저장 후 리스트 업데이트
        k += 1 # k번째..
    print(f'#{x}', (k-1)*n) # k=1로 시작했기 때문에 순서는 (k-1)번째