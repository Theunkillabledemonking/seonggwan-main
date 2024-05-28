# 별을 5 X 5
star_count = 5

# 1번 문제
for _ in range(star_count):
    for _ in range(star_count):
        print("*", end = "")
    print()
print()
# 2번 문제

star_count = 5

for _ in range(star_count):
    for _ in range(star_count):
        print("*" , end = "")
    print()

    star_count -= 1

# 3번 문제

row_count = 5
star_count = 1

for _ in range(row_count):
    for _ in range(star_count):
        print("*", end = "")
    print()

    star_count += 1

# 4번 문제

row_count = 5
blank_count = 4
star_count = 1

for _ in range(row_count):
    for _ in range(blank_count):
        print(" ", end = "")
    for _ in range(star_count):
        print("*", end = "")
    print()

    blank_count -= 1
    star_count += 1

# 5번 문제

row_count = 5
blank_count = row_count - 1
star_count = 1

for _ in range(row_count):
    for _ in range(blank_count):
        print(" ", end = "")
    for _ in range(star_count):
        print("*", end = "")
    print()

    blank_count -= 1
    star_count += 2

print()

for count in range (1,10):
    print("*", end = "")

    if count % 2 == 0:
        print("민정->원주->성식(성관이가 고르라고 말해라)->성관")

