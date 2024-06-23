# 입력 받은 문자열이 문장 내 있을 경우
    # 검색된 문자열에 대한 정보를 출력
    # 검색된 문자열의 개수
    # 검색된 문자열의 위치(들)
        # 위치는 문자열이 시작되는 인덱스를 기준으로 하며, 문장의 첫 번째 글자는 인덱스 0으로 한다
        # 예를 들어, "hello world"에서 "o"를 검색하면, 위치는 [4, 7]로 출력
    
    # 전체 문장에 대한 정보를 출력
        # 단어의 개수 (단어는 띄어쓰기로 구분)
        # 전체 문자 수 (공백과 개행 문자를 제외한 글자 수)
        # 줄 수
        
    # 입력받은 문자열이 문장 내 없을 경우 
        # 해당 문자열이 없음을 화면에 출력하고, 검색할 문자열을 재입력 받는다
        # 검색된 문자열이 있을 때 까지 반복한다.
        
    # 요구 사항
    # - 문자열 검색, 단어 개수와 줄 수 카운팅 알고리즘은 직접 작성할 것
    # - 파이썬에서 제공하는 문자열 관련 함수 사용 금지


# 문자열 검색을 위한 사전 입력 문장
while True:
    sentence = """pos pos hello  bar
    foo bar foo pos kin pos
    test test pos"""

    print(sentence)

    word_count = 0
    word_lines = 0
    
    index_list = []
    sentence_notpace = [index for index in sentence]
    sentence_space = [index for index in sentence.split()]
    
    # 문자열 검증
    while True:
        input_value = input("검색할 문자열을 입력하세요!")
        if input_value in sentence_space:
            break
        else:
            print("해당 문자열이 없습니다. 다시 입력해주세요")
      
    # 해당 문자열 찾기
    for i in sentence_space:
        if input_value == i:
            word_count += 1
    print(f"검색된 문자의 개수 : ", word_count)
        
   # 문자열의 인덱스 위치 찾기
    for i in range(len(sentence_notpace)):
        if input_value[0] == sentence[i]:
            index_list.append(i)
    print(index_list) 
    
    # 단어의 개수 파악
    num_count = 0
    for i in sentence_space:
        if i.split():
            num_count += 1
    print("단어의 개수 ", num_count)
    
    # 전체 문자 수 파악
    word_string = 0
    for i in sentence_notpace:
        if i.split():
            word_string += 1
    print("전체 문자의 수 : " ,word_string)
    
    # 줄 수 파악
    lines_count = 1
    for i in sentence_notpace:
        if i == "\n":
            lines_count += 1
    print("줄 수 :", lines_count)
    break
    
    # for i in (sentence_space):
    #     if num_count += i.split()
    
    
    # 개행 문자가 포함된 여러 줄 문자열 출력
    
    

    # """ """ 구문은 여러 줄 문자열(Multiline string)을 정의하는데 사용된다.
    # 이를 활용하여 개행 문자가 포함된 여러 문자열을 효율적으로 작성할 수 있다.
    
    

    
    
    