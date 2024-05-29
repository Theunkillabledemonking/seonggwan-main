# h의 개수를 출력
myString = "hello hyndai hoho"

count = 0

for str_h in myString:
    if str_h == "h" :
        count += 1

print("문자열 내 h 갯수 : ", count)