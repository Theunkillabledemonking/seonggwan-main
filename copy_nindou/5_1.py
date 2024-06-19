# 사용자로부터 세개의 정수 입력 받기
numbers = [int(input(f"{i}번째 수 입력 : ")) for i in ["첫", "두", "세"]]

# 값 비교
max_number = numbers[0]
for i in numbers:
    if i >= max_number:
        max_number = i

# 출력
numbers_set = set(numbers)
# 중복된 요소를 찾기
remove_num = [i for i in numbers if numbers.count(i) > 1]

# 같은 수
if numbers[0] != numbers[1] != numbers[2]:
    print(f"모든 수가 다릅니다. 가장 큰 수는 {max_number}입니다.")
# 두 수가 같다
elif len(numbers_set) == 2:
    print(f"두 수가 같습니다. {remove_num[0]}")
# 모두 다르다
else:
    print(f"모든 수가 같습니다.{numbers[0]}")