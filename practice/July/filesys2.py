# bar = lambda x, y : x* y

# def Anonymous(x, y):
#     return x * y

# bar = Anonymous
# 람다 함수의 특징 함수의 이름의 특징이 없다 매개변수하고 실행할때 분리가 된다 
# 실행되는 코드가 한줄이고 반드시 리턴이됨
# 이 함수를 정의를 하면 메모리상의 위치가 리턴이 된다.

# bar = lambda x,y : x * y

# 솔트 할 때 사용한다

bar = [[10, 9], [2, 8], [3, 10]]

def get_value(record):
    return record[1]

result = sorted(bar, reverse=True) #[[10, 9], [3, 10], [2, 8]] 내림차순 변경
print(result)

result = sorted(bar, key = get_value, reverse=True) # get_value 함수를 정의해서 인덱스 1번째 기준으로 삼는다.
print(result)

result = sorted(bar, key = lambda record : record[1], reverse=True)
# 재사용 불가능한 함수를 쓰는것보다 람다를 이용해서 레코드 변수를 선언함과 동시에 1번째 인덱스로 기준 삼는다.
print(result)

result = sorted(bar, reverse=False) #[[2, 8], [3, 10], [10, 9]] 오름차순 변경
print(result)

# 매트릭스에서 기본으로 레코드값으로 값이 변경이 된다.
# 어떤 값 래코드마다 어떤 기준으로 줄을 세울것인지 정해야된다.
# 각 인덱스 0번째 기준마다 출력되게 

