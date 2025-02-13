# 스택
# 1. empty list를 스택으로 사용
# append(), pop() 메소드
# * top이 필요없음.
s = []
s.append(1); s.append(2); s.append(3)
while s: # 빈 스택이 아닐동안
    print(s.pop())
    print(s)

# 2. list를 사용하기는 하지만, 공간을 미리 생성한 채 사용
# -> 인덱스로 push()/pop() 구현, top이란? 가장 마지막에 저장된 값의 위치
# * 스택이 꽉 차있는지 확인하면서 push

size = 3
s = [0] * size
top = -1

def push(item): # 스택에 값을 저장
    global top
    # full 상태를 체크
    if top == size - 1:
        raise Exception('full')
    top += 1
    s[top] = item

def pop(): # 스택에서 꺼낸 값을 반환
    global top
    #empty 상태를 체크
    if top == -1:
        raise Exception('empty')
    ret = s[top]
    top -= 1
    return s[top] 

def isempty():
    return top == -1