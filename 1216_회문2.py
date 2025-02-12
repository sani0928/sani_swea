import sys; sys.stdin = open('1216input.txt')

# 가로 세로를 모두 체크해 가장 긴 회문의 길이를 체크한다.
# 길이 100의 회문을 찾고 없으면 길이 99의 회문을 찾고 없으면 길이 98의 회문을 찾고..
# 길이 i의 회문을 발견하면 함수를 종료하고 i를 반환한다.

def search(arr):

    for i in range(100,0,-1):

         # 가로로 순회
        for r in range(100):
            for c in range(100-i+1):
                slicing_r = arr[r][c:c+i]
                if slicing_r == slicing_r[::-1]:
                    return i
        
        # 세로로 순회
        for r in range(100):
            reverse_arr = [arr[c][r] for c in range(100)]
            for c in range(100-i+1):
                if reverse_arr[c:c+i] == reverse_arr[c:c+i][::-1]:
                    return i
                        
    return 0


for x in range (1,11):
    t = int(input())
    arr = [list(str(input())) for _ in range(100)]
    print(f'#{t}',search(arr))