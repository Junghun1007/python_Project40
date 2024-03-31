import random

initial_number = random.randint(1,100) # 정수 값 반환

game_count = 1

while True:
    try:
        input_number = int(input("1~100까지의 숫자 입력 : "))
        if input_number > initial_number:
            print("Down")
        elif input_number > initial_number:
            print("Up")
        else:
            print(f"Yeah! / try out : {game_count}")
            break
        game_count += 1 # 횟수 카운트
    except:
        print("Error: please input int not string") # 예외처리 후 재실행?
