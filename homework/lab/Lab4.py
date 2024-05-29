# For 사용하여서 문자열 내 단어 개수 출력

myString = "It is a great weather with you"

count = 0

for str_space in myString:
    if str_space == " ":
        count += 1
count += 1

print("문자열 단어 갯수 : ", count)