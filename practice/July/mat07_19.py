import random
def get_matrix(*args):
    
    if not (1 <= len(args) <= 2):
        return None
    
    matrix_row = args[0]
    
    if len(args) == 1:
        matrix_col = args[0]
    else:
        matrix_col = args[1]
        
    data_frame = {
        "num_row" : matrix_row,
        "num_col" : matrix_col,
        "data" :[[random.randint(1, 100) for _ in range(matrix_col)]\
         for _ in range(matrix_row)]
    }

    # 'data' 열의 각 행의 합계를 계산하여 'sum' 열에 저장
    # 람다 함수는 각 행에 대해 합계를 계산하는데 사용됩니다.
    # apply 메서드를 사용하여 데이터 프레임의 각 행에 대해 함수를 적용합니다.
    data_frame['sum'] = lambda : sum([sum(row) for row in data_frame['data']])
    
    # bar = [[random.randint(1, 100) for _ in range(matrix_col)]\
    #     for _ in range(matrix_row)]
    return data_frame

foo = dict()
foo['a'] = get_matrix(3,2)
foo['b'] = get_matrix(3,2)
foo['c'] = get_matrix(3,2)
foo['d'] = get_matrix(3,2)

result = sorted(foo.items(), key = lambda arg:arg[1]['sum']())
for item in result:
    print(item[1]['sum']())

# foo = (get_matrix(4,4))
# print(foo['num_row'], "\t" , foo['num_col'])
# print(foo['data'])
# print(foo['sum']())
# print(get_matrix())

