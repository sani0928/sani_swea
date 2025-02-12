import sys; sys.stdin = open('20396input.txt')

# n은 돌의 개수, m은 시도 횟수
# i번째부터 j번째까지 i번째 숫자로 변환
# 범위가 j번째 미만이면 최대 범위까지 변환

t = int(input())

for x in range(1, t+1):

    n,m = map(int,input().split())
    arr = list(input().split())

    for _ in range(m):
        i,j = map(int,input().split())

        # 문제에서 지정한 순서는 i-1번째이기 때문에 인덱스값 조정
        i += -1

        # input에서 정한 범위가 arr 범위를 벗어날 경우 arr 길이와 i+j 범위가 같아질 때까지 j를 1씩 낮춤

        if len(arr) < i+j:
            while len(arr) < i+j:
                j -= 1

        # i번째부터 j번째까지 i번째와 같은 돌로 치환
        for y in range(i, i+j):
            arr[y] = arr[i]
        # 잘못된 예시 : arr[i:i+j] = arr[i]
        
    print(f'#{x}', *arr)