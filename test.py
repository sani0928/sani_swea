
counts = 0


def function_a():
    global counts

    while count % 3 != 0:
        function_b()  # 나머지 경우 function_b 실행
    
    count += 1
    print("Function A 실행")


def function_b():
    global counts

    while count % 3 == 0:
        function_b()  # 나머지 경우 function_b 실행
    
    count += 1
    print("Function B 실행")

print(function_a())
