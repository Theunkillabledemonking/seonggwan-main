import random
import turtle

# 화면 설정
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width() // 2
height = screen.window_height() // 2

print("윈도우 가로X세로",width, height)
# 거북이를 생성합니다
t = turtle.Turtle()


# 거북이가 움직이는 함수를 정의
def move_foward():
    t.forward(100)
    x, y = t.position()
    
    if x > width or x <= -width or y > height or y <= -height:
        t.right(180)
    

def move_backward():
    t.back(100) 
    
def turn_left():
    t.left(15)
    
def turn_right():
    t.right(15)
# 펜 색깔을 검은색으로 변경 
def change_color_to_black():
    t.color("black")
    
def change_color_to_red():
    t.color("red")

# 펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))
    
# 키보드 이벤트를 설정
screen.listen()
screen.onkey(move_foward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_random, "c")
screen.onkey(change_color_to_black, "d")
screen.onkey(change_color_to_red, "r")

# i를 누르면 색깔이 빨간색 -> 검은색 또는 검은색이면 빨간색으로
# 현재 펜 색깔이 빨간색 또는 검은색인 경우에만 반전
def change_color_to_blared():
    current_color = t.pencolor()
    
    if  current_color == ("red"):
        t.pencolor("black")
    elif current_color == ("black"):
        t.pencolor("red")

screen.onkey(change_color_to_blared, "i")

def change_color():
    
    # 1 ~ 3 이외의 값 입력 시 재입력 
    
    while True:
        print("색깔 선택: ")
        print("1. 파란색")
        print("2. 검정색")
        print("3. 노란색")
        input_value = 0
        
        if not (1 <= input_value <= 3):
            input_value = int(input("숫자 입력"))
            
        if input_value == 1:
                t.pencolor("blue")
            
        elif input_value == 2:
                t.pencolor("black")
            
        elif input_value == 3:
            t.pencolor("yellow")  
        
        else:
            print("재입력")
            
        
        
        
      

screen.onkey(change_color, "t")
# 이벤트 루프를 시작

screen.mainloop()