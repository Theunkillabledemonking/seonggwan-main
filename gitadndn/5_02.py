# # 정수 * 출력

# input_Value=int(input())

# count = 0
# # "*"
# for i in range(0,input_Value):
#     i = "*"
#     print(i, end="")
# end = "" \t  \n

# print("he\tl\n\lo w\nor\n\ld")

# 입력 받은 정수 개수의 가로 x 세로 바둑판 출력 

input_value = int(input("입력"))
print()
# for i in range(0,input_value):
#     i = "*"
#     print(i * 3)
    
for i in range(0,input_value):
    for i in range(0,input_value): # 세로 
        print("*", end="")
    print() # 가로
