# import random
# # 단어 입력 3번
# input_list = []
# for i in range(3):
#     while True :
#         input_value = input("단어를 입력하세요")
#         if 5 <= len(input_value) <= 20:
#             input_list.append(input_value)
#             break
#         print("5 이상 20 이하 입력")
# print(input_list)

# word_select = list(input_list[random.randint(0, 2)])
# print(word_select)
# word_print = word_select[:]
# print(word_print)

# # 글자 수 반올림 처리
# char_num_word = len(word_select)
# blind_num_word = char_num_word / 2
# if blind_num_word < char_num_word // 2:
#     blind_num_word += 1
    
# blind_num_word = int(blind_num_word)
# print(blind_num_word)
# # 블라인드 처리
# blind_num_list = [index for index in range(0, char_num_word)]
# print(blind_num_list)

# for index in range(1, char_num_word - blind_num_word):
#     del blind_num_list[random.randint(0, len(blind_num_list) - 1)]
# print(blind_num_list)
# # 사용자 입력

# for index in blind_num_list:
#     word_print[index] = "_"
# print(word_print)

# while len(blind_num_list):
#     print(word_print)
#     find_list = []
    
#     input_value = input("입력하세요")
#     for index in blind:
#         if word_select[index] == input_value:
#             word_print[index] = input_value
#             find_list.append(index)
            
#     for f_index in find_list:
#         blind_num_list.remove(f_index)
        
# print(word_print)

# argument(인자값)

# 1) positional argument 위치 인자값

# def foo(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)

# foo(1, 2, 3)

# # 2) keyword argument 
# def pos(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)
    
# pos(arg_c = 1, arg_a = 2, arg_b = 3)

# 3) default argument
# a) 모든 파라미터에 초기값을 설정한다.
# b) 초기 값을 가지는 파라메터는 제일 뒷쪽에 위치한다.
# def bar(arg_a = 5, arg_b = 6, arg_c = 7, argc_d = 8):
#     print(arg_a, arg_b, arg_c, argc_d)

# bar()
# bar(1)
# bar(1, 2)
# bar(1, 2, 3)
# bar(1, 2, 3, 4)


# variable parameter : 가변 파라메터
# 1) *
# 2) **
        # * -> 가변 : tuple로 받겠다
# def foo(*args):
#     print(len(args))
#     for value in args:
#         print(value)

# foo(1)
# foo(1,2,3,4,5,6,7,8,9,10,11,12)

# 1) * -> 가변 : tuple로 받겠다.
# def bar(*args):
#     if len(args) == 1:
#         start = end = args[0]
#     elif len(args) == 2:
#         start, end = args
#     else:
#         return
    
#     for dan in range(start, end + 1):
#         for num in range(1, 10):
#             print(f"{dan} * {num} = {dan*num}")
            

def foo (arg_a, arg_b, arg_c, arg_d, arg_e):
    print (arg_a, arg_b, arg_c, arg_d, arg_e)

# foo -> (1, 2, 3, 4, 5)

#arg_list = [value for value in range(1, 6)]
arg_list = [1, 2, 3, 4, 5, 6]

foo (*arg_list)
