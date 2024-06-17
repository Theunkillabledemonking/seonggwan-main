# 1~1000까지의 정수 중 3의 배수의 총합 구하기

count = 0
sum = 0

while count <= 1000 :
    count += 1
    if count % 3 == 0 :
        sum += count
print("1~1000 사이 정수 중 3의 배수의 총 합은 :", sum)
    
    