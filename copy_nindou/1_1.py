age = int(input("나이를 입력하세요"))
msg_li = "{}입니다."

if age <= 12:
    msg = "어린이."
elif 12 < age <= 18 :
    msg = "청소년."
else:
    msg = "어른."

print(msg_li.format(msg))