# 리스트와 타겟 숫자를 매개변수로 받아
# 타겟 숫자가 리스트 내에 있는지 여부 반환 함수

def contains(lists, target):
    # for index in range(len(lists)):
    for value in lists:
        if value == target:
            return True
    return False

print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))