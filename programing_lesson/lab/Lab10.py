# 컴퓨터 1 ~ 100 랜덤 숫자 선택

# 사용자는 숫자를 맞추기 위해 시도, 사용자에게 10번의 기회가 주어진다

# 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "더 큰 숫자입니다." 출력

# 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "더 작은 숫자입니다" 출력

# 사용자가 숫자를 맞추면 "정답입니다!" 라고 출력되고 게임 종료

# 10번의 시도가 끝날 때 까지 숫자를 맞추지 못하면 모든 기회를 사용하였습니다 정답은 [숫자]입니다. 출력

# 사용자가 0을 입력하면 게임이 종료됨

import random

random_computer = random.randint(1, 100)
count = 0
print(random_computer)

# 10번 반복
while count < 10 :
    random_user = int(input(f"기회 {count+1}/10 - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): "))
    
    # 0 입력시 바로 프로그램 종료
    if random_user == 0 :
        print("겜을 종료합니다.")
        break
    
    # 숫자 비교
    if random_computer > random_user :
            print("더 작은 숫자 입니다.")
    elif random_computer < random_user :
            print("더 큰 숫자 입니다.")
    else:
        print("정답입니다. \n게임이 끝났습니다.")
        break
    
    count += 1
    # 게임종료 문구
if count == 10: 
    print(f"모든 기회를 사용하셨습니다. 정답은 {random_computer}입니다.")
    print("게임이 끝났습니다.")
