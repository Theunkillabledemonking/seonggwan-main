book_list = []
while True:
    book = input('도서 제목을 입력하세요 종료 하려면 ㅇㄹ')
    if book == "종료":
        break
    book_list.append(book)
print(f"도서 목록 : {book_list}")