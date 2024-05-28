# 점수 리스트 두학기의 점수를 연속해서 포함

# 리스트위 앞부분은 1학기 뒷부분은 2학기 점수

scores = [88, 92, 75, 65, 79, 84, 91, 87, 90, 88]

first = scores[:4]
second = scores[4:]

pss_mx = max(first)
pss_mz = max(second)

print(f"1학기 최고 점수: {pss_mx}")
print(f"2학기 최고 점수: {pss_mx}")