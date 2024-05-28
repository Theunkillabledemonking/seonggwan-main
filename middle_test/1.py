# # # 두개의 실수를 입력받아


    

# # input_Value1 = float(input("첫 번째 값을 입력 하세요"))
# # input_Value2 = float(input("두 번째 값을 입력 하세요"))
# # #이 후 사용 할 +, - * / 중 하나 입력

# # Operator = input("연산자를 선택 하세요 (+, -, *, / 중 하나 입력)")

# # code_type = input("결과 값 자료형(integer, float, string 중 하나 입력)")

# # if Operator == '+':
# #    result = input_Value1 + input_Value2

# # elif Operator == '-':
# #    result = input_Value1 - input_Value2
    
# # elif Operator == '*':
# #    result =  input_Value1 * input_Value2
    
# # elif Operator == '/':
# #     result = input_Value1 / input_Value2

# # if code_type == 'integer':
# #    result = int(result)
   
# # elif code_type == 'float':
# #    result = float(result)
  
# # elif code_type == 'string':
# #    result = str(result)
   
# # print(f"결과 값은 아래와 같습니다.")
# # print(f"{input_Value1} {Operator} {input_Value2} = {result}")

# # # 결과 값 자로형 (integer, float, string 중 하나 입력)





# # 사용자에게 두개의 실수를 입력 받아라. 
# input_value1 = float(input("첫 번째 값을 입력 하세요:"))
# input_value2 = float(input("두 번째 값을 입력 하세오:"))
# # 사용할 연산자를 선택

# operator = input("연산자를 선택 하세오 (+, -, *, / 중 하나 입력)")

# num = 0

# if operator == "+":
#    num = input_value1 + input_value2
# elif operator == "-":
#    num = input_value1 - input_value2
# elif operator == "*":
#    num = input_value1 * input_value2
# elif operator == "/":
#    num = input_value1 / input_value2

# finally_if = input("결과 값 자료형(integer, float, string 중 하나 입력)")

# if finally_if == 'integer':
#    num = int(num)
# elif finally_if == 'float':
#    num = float(num)
# elif finally_if == 'string':
#    num = str(num)

# print("결과 값은 아래와 같습니다.")
# print(f"{input_value1} {operator} {input_value2} = {num}")

# # 최종적으로 결과를 원하는 자료형으로 출력하는 프로그램 작성





# 두개의 실수를 입력받아
number1 = (input("첫 번째 값을 입력 하세요\n"))
if '.' in number1:
   number1= float(number1)
else:
   number1= int(number1)
number2 = (input("두 번째 값을 입력 하세요\n"))
if '.' in number2:
   number2= float(number2)
else:
   number2= int(number2)
# + - * / 연산자를 선택하여
operator = input("연산자를 선택 하세요 (+, -, *, / 중 하나 입력)\n")
select_data = input("결과 값 자료형(integer, float, string 중 하나 입력)\n")

total = 0

#연산자 선택
if operator == '+':
    total = number1 + number2
elif operator == '-':
    total = number1 - number2
elif operator == '*':
    total = number1 * number2
elif operator == '/':
    total = number1 / number2
# 원하는 자료형으로 출력

# 결과값 원하는 자료형
if select_data == 'integer':
   total = int(total)
elif select_data == 'float':
   total = float(total)
elif select_data == 'string':
   total = str(total)



print("결과 값은 아래와 같습니다.")
print(f"{number1} {operator} {number2} = {total}")

