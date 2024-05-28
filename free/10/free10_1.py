# 빈 리스트를 생성합니다.
books = []

# 사용자 입력을 처리하는 루프를 시작
while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    if title == '종료':
        break
    # 여기서 도서 제목을 리스트에 추가하는 코드 작성해라
    books.append(title)
# 최종 도서 목록을 출력한다
print("도서 목록:", books)
