with open('example.txt', 'r+') as file:
    content = file.read()
    print("Original Content", content)
    file.seek(0) # 파일의 시작 위치로 포인터 이동
    file.write('Updated Content')