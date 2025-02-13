# 카운팅이란, 출현 빈도수 계산

# dictionary에서의 카운팅
# 해시테이블 개념이 포함되어 있음.

lst = [0, 4, 1, 3, 1, 2, 4, 1]

val_dict = {}
for key in lst:
    if key in val_dict: # key가 dict에 있니?
        val_dict[key] += 1 # 있으면 카운팅
    else:
        val_dict[key] = 1 # 없으면 key를 추가
        
    # val_dict[key] = val_dict.get(key, 0) + 1 # get를 이용해 if문 축약

print(val_dict) #{0: 1, 4: 2, 1: 3, 3: 1, 2: 1}

# 배열에서의 카운팅 = 값을 배열의 인덱스를 사용하겠다.
# 주의사항 : 값이 0 이상, 양의 정수에 해당되어야 함.
# 배열의 공간이 있어야 함. (배열의 범위 지정) *범위가 과도하게 커지면 비효울성 증가

data = [0, 4, 1, 3, 1, 2, 4, 1]
N, K = 8, 4

counts = [0] * (K + 1)
for val in data:
    counts[val] = counts[val] + 1
    # ex) counts = [1, 0, 0, 0, 1]일 때, counts[4] + 1 하면 counts = [0, 0, 0, 0, 1]

print(counts)
    
