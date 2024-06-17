
color = input("put the color: ")

maker = ""

bmw_list = ["M1", "M2", "M3"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_genesis = ["G80", "G90"]

list_model = [bmw_list, list_tesla, list_lexus, list_genesis]
list_maping = []

# 회사 목록을 가지고 온다. : 반복 -> 4회 -> bmw, tesla, lexus, genesis
# 세로 반복 
maker_name_list = ["bmw", "tesla", "lexus", "genesis"]
index_count = 0

for maker_list in list_model :
    # 회사별 자동차 모델을 가지고 온다 -> 반복 횟수? 회사 별 모델 개수에 따라 다름.
    # 가로 반복
    for mode_in_list in maker_list :
        if color == mode_in_list :
            maker = maker_name_list[index_count]
            break
        
    if maker != "":
        break
            # maker = "bmw" 또는 "lexus"
            # 해당 모델을 선택
            
    index_count += 1

#dup_found = False

# if color in bmw_list :
#     maker = "bmw"
# elif color in list_tesla:
#     maker = "tesla"
# elif color in list_lexus:
#     maker = "lexus"
# elif color in list_genesis:
#     maker = "genesis"
# else:
#     maker = "unkown model"
    
# print(maker)

if maker == "" :
    for _ in bmw_list :
        if color == _ :
            maker = "BMW"
            break
            # dup_found = True
if maker == "" :
    for _ in list_tesla :
        if color == _ :
            maker = "Tesla"
            break
            # dup_found = True
if maker == "" :
    for _ in list_lexus:
        if color == _ :
            maker = "Lexus"
            break
            # dup_found = True
if maker == "":
    for _ in list_genesis :
        if color == _ :
            maker = "Genesis"
            break
            # dup_found = True

maker = maker if maker != "" else "알 수 없는 모델"
print(maker)

    
