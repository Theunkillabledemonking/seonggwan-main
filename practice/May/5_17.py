# 바다코끼리 연산자 :=
# 대입(Assignment)과 평가(Evaluation) -> 사용
# msg = "hello"

# for char in msg: # hello -> 1st : h, 2st : e, 3st : 1, 4st: 1
#     print(msg)

# #msg = "hello"

# for char in (msg := "hello"): # hello -> 1st : h, 2st : e, 3st : 1, 4st: 1
#     print(msg)


# 삼항연산자

# msg = ""
# value = 1

# if value == 1:
#     msg = "안녕"

# else:
#     msg = "hello"

# print(msg)
# value = 1
# msg = "안녕" if value == 2 elif value == 3 else "hello"
# print(msg)

# stirke_out = True

# print("패배" if stirke_out else "승리")

# if stirke_out:
#     print("패배")
# else:
#     print("승리")

# 알고리즘
# 특정용어를 설명할려고하는 명령어

# value_1 = int(input("1st 값 :"))
# value_2 = int(input("2nd 값 :"))

# sum = value_1 + value_2

# print(sum)

import turtle

# 화면 생성 후 거북이가 그릴 수 있는 캔버스 생성
screen = turtle.Screen()

# 그림을 그릴 거북이 객체를 생성
t = turtle.Turtle()
t.color("hot pink")
t.speed(10)
# 세번 반복 직사각형
# for _ in range(3):
    # 거북이 앞으로 100만큼 이동
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)
t. end_fill()

t.penup()
t.goto(-50, 50)  # 글자의 위치 조정
t.pendown()
t.color("pink")
t.write("てめ　サンキュー　だ！", align="center", font=("Arial", 24, "bold"))

for _ in range(5):
    t.color("light blue")
    t.forward(100)
    t.right(144)
# 터틀 그래픽 창이 닫히지 않고 유지
turtle.done()