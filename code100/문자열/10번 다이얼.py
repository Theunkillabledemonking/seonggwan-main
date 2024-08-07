# 2 3 4 5 6 7 8 9
# 2 1

number_letters = {
    '3' : ['A', 'B', 'C'],
    '4' : ['D', 'E', 'F'],
    '5' : ['G', 'H', 'I'],
    '6' : ['J', 'K', 'L'],
    '7' : ['M', 'N', 'O'],
    '8' : ['P', 'O', 'R', 'S'],
    '9' : ['T', 'U', 'V'],
    '10' : ['W', 'X', 'Y', 'Z']
}

count = 0

a =input()
new = []
for i in a:
    new.append(i)
    
for i in new:
    for key, value in number_letters.items():
        if i in value :
            count += int(key)


print(count)