# # 사용자로부터 여러개의 숫자를 입력 받음
# number_str = input("숫자들을 쉼표로 구분하여 입력하세요:")
# # 문자열을 개별 숫자로 분리
# numbers = number_str.split(',')
# # 갓 숫자를 정수로 변환 후 모든 숫자의 합을 계산한다.

# count = 0 # 합

# #숫자 리스트를 정수로 형변환 후 합계 더함
# for num_str in numbers:
#     num = int(num_str)
#     count += num

# #숫자가 100을 초과하지 않은 경우 최종 총합과 입력된 숫자들을 출력
# if count < 100 :
#     print("총합이 100을 초과하지 않았습니다.")
#     print("입력된 모든 숫자들:",numbers)
#     print("최종 총합: ",count)

# #숫자가 100을 초과하면 해당 순간의 입력값들과 총합 출력하고 종료
# else:
#     print("총합이 100을 초과하였습니다.")
#     print("입력된 모든 숫자들:",numbers)
#     print("최종 총합: ",count)


input_num_list = input("숫자를 입력하세오:")

num_list = input_num_list.split(",")
sum = 0
output_list = []
over_100_flag = False # 

for num_str in num_list:
    num = int((num_str))
    sum += num
    output_list.append(num)

    if sum > 100:
        over_100_flag = True # break가 동작
        break

if over_100_flag:
    print("총합이 100을 초과하였습니다.")
    print("현재까지의 입력값들:",output_list)
    print("현재까지의 총합", sum)
else:
    print("총합이 100을 초과하지 않았습니다.", sum)
    print("최종 총합", output_list)
