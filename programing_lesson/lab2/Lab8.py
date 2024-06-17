# 가변 개수의 숫자를 매개변수로 받아 평균을 반환

def calculate_average(*args):
    total = sum(args)
    count = len(args)
    avg = total / count
    return avg

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))