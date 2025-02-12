import sys; sys.stdin = open('22375input.txt')

# # 앞에서부터 i번 스위치라고 가정한 채 하나씩 스위치 눌러서 결과와 비교
# # 결과와 같은 상태가 발견되면 해당 i번 출력
# # 끝까지 눌렀는데 결과와 같은 상태가 발견되지 않으면 다음 상태 반복

t = int(input())

for x in range(1, t+1):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    # 초기상태에서 i=0 ~ i=n까지 한번씩 눌러보기



'''
111 / 000, 100, 110
011 / 100, 000, 010
001 / 110, 010, 000
'''