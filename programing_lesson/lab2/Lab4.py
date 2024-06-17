# 세 개의 숫자를 매개변수로 받아 가장 큰 값으로 반환

def max_of_three(arg_a, arg_b, arg_c):
    # max_value = arg_a
    
    # if arg_b > max_value:
    #     max_value = arg_b
    
    # if arg_c > max_value:
    #     max_value = arg_c
        
    # return max_value

    values = [arg_a, arg_b, arg_c]
    max_value = values[0]

    for value in values:
      if value > max_value:
          max_value = value
          
    return max_value

print(max_of_three(10, 20, 15))