import random

# 주사위를 n번 던졌을 때 각 번호가 나올 확률을 계산
# 주사위 1 ~ 6 까지의 숫자
while True:
    trail_count = int(input("숫자를 입력하세요."))
    if 100 <= trail_count <= 1000000:
        break
    

dice_list = [0, 0, 0, 0, 0, 0]

# trial_count 만큼 랜덤 숫자를 발생 : 1 ~ 6
for _ in range(trail_count):
    # 생서된 랜덤 값에 따른, 각 주사우 번호의 횟수를 증가
    rand_num = random.randint(1, 6) # 자료구조를 잘 형성하면 식이 간단하다.
    
    dice_list[rand_num - 1] += 1
    
max_event = -1

for index in range(6):
    if dice_list[index] > max_event:
        max_event = dice_list[index]
print(max_event)

print(dice_list)

#for index in dice_list:
#    if dice_list > max_event:
        
# 히스토그램과 확률을 계산
# 주사위 1이 나올 확률 : ( E1 / trial_count ) * 100 -> 정보과학
for i in range(6):
    print("*" * int(dice_list[index] / max_event * 10), "\t", end="")
    print(f"{i+1} 번 확률 : {(dice_list[i] / trail_count) * 100}")

