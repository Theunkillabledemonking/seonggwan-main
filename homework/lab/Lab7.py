# # # # 높이가 5인 다이아몬드 출력
    
# height = 5
# a_height = height - 1

# # 별을 점차 증가
# for i in range(height):
#     spaces = " " * (a_height - i)
#     stars = "*" * (i * 2 + 1)
#     print(spaces + stars)

# # 공백을 점차 증가
# for i in range(a_height):
#     spaces = " " * (i + 1)
#     stars = "*" * (2 * (a_height - i) -1)
#     print(spaces + stars)

# for i in range:
#     print(" " * (4 - i) + "*" * (i * 2 + 1))
# for i in range:
#     print(" " * (i + 1) + "*" * (7 - (2 * i)))
    
    
    
    
    
    
    
# height = 5
# a_height = height - 1
# for index in range(0,5):
#    print((" " *  (height - index)) + ("*" * (index * 2 + 1) )) 
# for index in range(height ,0 ,-1):
#     print(" " * (height - index)) + ("*" * (2 * (a_height - index)) -1)






# height = 5
# a_height = height -1

# # 점차 플러스
# for index in range(height):
#     space = (" " * (a_height - index))
#     stars = ("*" * (index * 2 + 1))
#     print(space + stars)

# # 점차 마이너스
# for index in range(a_height):
#     space = (" " * (index + 1))
#     stars = ("*" * (2 * (a_height - index)-1))
#     print(space + stars)
    
        
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
    stars = "*" *(2 * (a_height - i) - 1)
    print(spaces + stars)
