bar = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
]

bar[0][1][2]

# [2][3][3]
# 3 X 3 Matrix가 2장


# 첫 번째 : 1번째 Matrix가 반환
# 두 번째 : 2번쨰 Matrix가 반환
for matrix in bar:
    for row in matrix:
        for col in row:
            print(col, "\t", end="")
        print()
    print("-" * 10)