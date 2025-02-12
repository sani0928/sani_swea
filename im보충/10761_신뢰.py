import sys; sys.stdin = open('10761input.txt')

def fastest_time(commands):
    orange_pos, blue_pos = 1, 1  # 오렌지와 블루의 초기 위치
    orange_queue = []  # 오렌지가 눌러야 할 버튼 리스트
    blue_queue = []    # 블루가 눌러야 할 버튼 리스트

    # 로봇별로 버튼 리스트 저장
    for robot, button in commands:
        if robot == 'O':
            orange_queue.append(button)
        else:
            blue_queue.append(button)

    total_time = 0  # 전체 시간
    orange_idx, blue_idx = 0, 0  # 각 로봇의 현재 버튼 인덱스

    for robot, target_button in commands:
        total_time += 1  # 버튼을 누르는 시간

        if robot == 'O':
            # 오렌지 로봇이 목표 버튼까지 이동
            move_time = abs(orange_pos - target_button)
            orange_pos = target_button  # 버튼을 누른 후 위치 업데이트

            # 버튼 누를 때까지 걸린 시간과 대기 시간 비교
            if move_time >= total_time:
                total_time = move_time + 1  # 이동 후 버튼 누르기

            orange_idx += 1  # 다음 버튼 준비

        elif robot == 'B':
            # 블루 로봇이 목표 버튼까지 이동
            move_time = abs(blue_pos - target_button)
            blue_pos = target_button  # 버튼을 누른 후 위치 업데이트

            if move_time >= total_time:
                total_time = move_time + 1  # 이동 후 버튼 누르기

            blue_idx += 1  # 다음 버튼 준비

    return total_time


# 입력 처리
TC = int(input())
for test_case in range(1, TC + 1):
    data = input().split()
    N = int(data[0])  # 버튼 개수

    commands = []  # (로봇, 버튼) 형태로 저장
    for i in range(1, len(data), 2):
        robot = data[i]
        button = int(data[i + 1])
        commands.append((robot, button))
    print(commands)

    # 결과 출력
    result = fastest_time(commands)
    print(f"#{test_case} {result}")
        