# # 높이가 5인 다이아몬드 출력
    
height = 5
a_height = height - 1

# 별을 점차 증가
for i in range(height):
    spaces = " " * (a_height - i)
    stars = "*" * (i * 2 + 1)
    print(spaces + stars)

# 공백을 점차 증가
for i in range(a_height):
    spaces = " " * (i + 1)
    stars = "*" * (2 * (a_height - i) -1)
    print(spaces + stars)
 
#print(" " * (4 - i) + "*" * (i * 2 + 1))
#print(" " * (i + 1) + "*" * (7 - (2 * i)))