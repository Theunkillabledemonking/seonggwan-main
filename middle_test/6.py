# 10 ~ 20 사이 정수 중 짝수의 합을 계산

sum = 0

for value in range(10, 21, 2):
    sum += value
    
print(value)
    

# for i in range(10, 21):
#     if i % 2 == 0 :
#         sum += i
        
print(sum)

# 구구단 

# 2단부터 9단 까지
# 2 X 1 = 2
# 2 X 2 = 4
#
# 2 X 9 = 18
#------------
#
# 9 X 9 = 콘

for value in range(2,10): # 2단 -> 9단 : 5단과 7단은 제외
    if value == 5 or value == 7:
        continue

    for index in range(1,10):
        print(value, "X", index, "=" , value * index)
    print("--------------------------------------")