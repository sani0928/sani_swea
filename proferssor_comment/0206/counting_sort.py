'''
data에서 각 항목들의 발생 횟수를 정수로 인덱스 되는 카운트 배열을 만든다.


초기 카운트 항목들은 0이며 각 항목들의 발생 횟수에 따라 +1씩 증가한다.

0 <= data[i] <=4 : 조건
counts = [0] * 5 # max(count) + 1
'''

data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0, 0, 0, 0, 0]
N= len(data)
for i in range(N):
    counts[data[i]] += 1