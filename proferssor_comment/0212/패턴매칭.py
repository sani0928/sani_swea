def check_palindrome(arr, n, l): #n은 전체 길이, l은 회문의 길이
    count = 0
    for s in range(n-l+1):
        e = s+l-1
        for i in range(l//2):
            if arr[s+i] != arr[e-i]:
                break
        else:
            count += 1
    return count

ret = 0
for row in arr:
    ret += check_palindrome()

# = = = = = = = = = = = = = = = = = = = =



'''
패턴 매칭 문제 => 텍스트에서 패턴이 존재하는 모든 위치를 찾는 문제
텍스트 => t[], 패턴 => p[]
텍스트의 특정 위치 => i, 패턴의 특정 위치 => j
패턴 매칭 알고리즘을 볼때
일치할 때 t[i] == p[j]
불일치할 때 t[i] != p[j]
'''
p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACACGTACCTACGACATTCCCTGCGCCGCCACCCGTTGAA"
n, m = len(t),len(p)

i=j=0
while i < n:
    # i=n이 되면 패턴 없음, j=m이면 찾은거임
    if p[j] != t[i]:
       i = i - j + 1 # i-j는 패턴 시작위치
       j = 0
    else:
        i,j = i+1, j+1

    if j == m:
        print(t[i-j:i-j+m])
    j = 0 # j는 다시 0으로 돌아감 (p[0]부터)
# = = = = = = = = = = = = = = = =
# 텍스트에서 패턴이 있을 수 있는 모든 시작 위치

p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACACGTACCTACGACATTCCCTGCGCCGCCACCCGTTGAA"
n, m = len(t),len(p)

while i <= n - m:
    for i in range(n-m+1):
        for j in range(m):
            if p[j] != t[i+j]:
                break
        else:
            print(t[i:i+m])
            i += m
            continue
        i += 1

