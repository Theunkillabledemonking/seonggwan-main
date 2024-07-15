# 사용자한테 행과 열의 수를 입력 받기
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# 행과 열의 수에 따라 2차원 리스트 생성
matrix = [[0] * cols for _ in range(rows)]
# 리스트 값 입력
for row in range(rows):
    for col in range(cols):
       matrix[row][col] = int(input(f"Enter value for [{row}][{col}] :"))
# 리스트 출력
for col in matrix:
    for row in col:
        print(row, "\t", end="")
    print()
