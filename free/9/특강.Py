
input_number ="990229-1234567"
check_number = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# 유효성 검사

# 주민번호 12자리를 자리별 체크 값과 곱한 후 더한다.
# 주민번호 12자리 : 0번째 index -> 11번쨰 index
sum = 0
count = 0

preprocessed_number = ""
for num in input_number:
    if num != "-":
        preprocessed_number += num
        
print(preprocessed_number)
print(preprocessed_number[:-1])

# #for num in input_number:
#     if num != "-" and count < 12 :
#         sum += int(num) * check_number[count]
#         count += 1
        

# 체크값을 계산한다 : (11 - (sum % 11)) % 10 == input_number[-1]
check_value = (11 - (sum % 11)) % 10 
# 판별 결과 값을 출력한다.
# 시험문제 잘 푸는 법 입력값을 안 넣고 검사를 다 한뒤 변수를 만들어서 테스트를 해라.
if check_value == int(input_number[-1]):
    print("유효한 주민번호")
else :
    print("유효하지 않은 주민번호")