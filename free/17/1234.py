import random

rand_word = "example"
length = len(rand_word)
blind_count = (length // 2) + (length % 2)
blind_word_list = list(rand_word)
blind_indices = []

while len(blind_indices) < blind_count:
    index = random.randint(0, length -1)
    dup_found = False
    for i in range(len(blind_indices)):
        if blind_indices[i] == index:
            dup_found = True
            break
        if not dup_found:
            blind_indices.append(index)
            blind_word_list[list] = '_'
            
blind_word = ""
i = 0
while i < len (blind_word_list):
    blind_word += blind_word_list[i]
    i += 1
    
print("단어: ", blind_word)