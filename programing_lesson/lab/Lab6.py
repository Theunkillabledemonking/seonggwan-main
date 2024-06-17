# 1 부터 20 까지의 숫자 중 홀수를 건너뛰고 컨티뉴 짝수의 합계
count = 0

for i in range(1, 21):
    if i % 2 != 0 :
        continue
    count += i
    
print("1부터 20까지의 짝수 합계 (홀수 건너뜀): ", count)
        
