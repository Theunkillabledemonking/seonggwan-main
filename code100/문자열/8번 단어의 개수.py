word = input()
word_1 = [index for index in word.split()]
count = 0

for i in word_1:
    if i.split():
        count += 1


print(count)