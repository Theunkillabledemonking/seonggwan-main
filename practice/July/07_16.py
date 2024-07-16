# 1차원 자료구조 - > list

# 1 ~ 100 사이 숫자 10개를 리스트에 저장하라

import random

# matrix
bar = {"a" : 10, "b" : 20, "f": 1, "d" : 9}
result = sorted(bar.items()) # 개층분류를 해서 자료구조이 가능하다.
print(result)

bar = [
        [
            [13, 8], [55, 85]
        ],
        [
            [10, 20], [30, 40]
        ],
        [
            [40, 50], [60, 70]
        ]
]

# [[matrix], [matrix], [matrix]]
def get_value(bar):
    return sum ([item for record in bar for item in record]) # 파이썬으로 나이스하게 가능하다.
    # sum = 0
    # for record in bar:
    #     for item in record:
    #         sum += item
    # # 매트릭스의 전체 함수의 핪
    # return sum

result = sorted(bar, key = get_value, reverse=True) # 첫번째 브라켓의 원소단위로 정렬을 한다.

#result = sorted(bar, key = "항목 간 비교 시 비교 값 정령 알고리즘", reverse=True) # 첫번째 브라켓의 원소단위로 정렬을 한다.
# 수의 크기로 정렬을 기준 잡았다.
print(result)
