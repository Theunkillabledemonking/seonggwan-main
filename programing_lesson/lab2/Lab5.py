#수가 짝수인지 홀수인지 판별

def is_even(number = None):
    if number % 2 == 0:
        return True
    # else: 사용  x
    return False
        
print(is_even(4))
print(is_even(5))