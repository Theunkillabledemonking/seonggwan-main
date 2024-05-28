# 파이썬 리스트를 사용하여 쇼핑
# 품목들을 관리하는 간단한 프로그램


# shopping_list 빈 리스트 생성
shopping_list = []

# 다음 품목을 추가
shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')
shopping_list.append('apple')
# print함수 이용해 현재 쇼핑리스트 내용출력
print("현재 쇼핑 리스트: ",shopping_list)
# toilet paper가 빠져 있는 것을 발견 후, 리스트 맨 앞에 추가
shopping_list.insert(0,'toilet paper')
# orange juce 리스트 두번째 위치에 추가
shopping_list.insert(1,'orange juce')
# 마지막으로 chicken, rice를 리스트에 추가해야하는데, 

shopping_list.extend (['chicken', 'rice'])
# 이품목을 한번의 연산으로 리스트에 추가해라.
print("최종 쇼핑 리스트: ",shopping_list)
