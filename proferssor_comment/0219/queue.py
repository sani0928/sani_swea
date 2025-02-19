# 자료구조 -> 저장소(연속적인 공간, 흩어서 저장) + 연산(함수/메서드도 구할 수 있다)
QSIZE = 4
Q = [0] * QSIZE
front = rear = -1

# 선형 큐의 경우

def enqueue(item):
    global rear
    # 주의
    if rear == QSIZE - 1:
        print('*full*')
        return
    
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    # 주의
    if front == rear:
        print('*empty*')
        return
    
    front += 1
    return Q[front]

# 원형 큐의 경우

# 모듈연산 작동 과정
# 일반적인 범위 내에서 작동할 땐 (0~n-1)%n은 정상적으로 동일한 인덱스 값이 나오지만
# 범위를 벗어나면 (n) 다른 결과가 나온다. (비커즈 n%n = 0)

def enqueue(item):
    global rear
    # 주의
    if front == (rear + 1) % QSIZE: # %n이 front의 값이 나온다는 것은 front == rear
        print('*full*')
        return
    
    rear += 1
    Q[rear] = item