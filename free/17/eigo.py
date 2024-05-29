# 단어 입력
# 키보드로부터 영어 단어 3개 입력 받아 리스트에 저장
# 단어의 글자 범위는 5 이상,20 이하로 제한
# 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구합니다

# 단어 선택 
# 입력된 3개 중 한개의 단어를 임의로 선택한다

# 게임 시작
# 선택된 단언의 글자 중 50%를 blind 처리합니다
# blind 처리된 알파벳은 랜덤하게 선택됩니다
# 예를 들어, 선택된 단어가 starbucks인 경우, 글자 수는 9자입니다
# 9/2 = 4.5 이므로 올림하여 5자를 blind 처리합니다
# 올림 알고리즘을 직접 구현하면 이를 위한 함수를 사용하지마세요
# 즉 파이썬에서 제공하는 올림 함수를 사용하지 않고, 직접 알고리즘을 작성하세요

# 알파벳 입력
# 키보드로 부터 알파벳 한글자를 입력받습니다.

# blind 해제 
# 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제합니다
# 존재하지 않을 경우 "없을" 메시지를 출력합니다

# 게임 종료
# 단어의 모든 글자를 맞출 경우 게임이 종료된다

# 결과 출력
# 게임 종료 시 시도 횟수를 출력합니다.
import random

str_list = []
str_count = 0
start_list = ["첫", "두", "세"]

# 조건에 맞는 리스트 입력
while str_count <= 2:
    while True:
        str_word = input(f"{start_list[str_count]}번째 단어를 입력하세요")
        if 3 <= len(str_word) <= 20 :
            str_count += 1
            str_list.append(str_word)
            break
        else:
            print("3 이상 20이하 글자로 구성된 단어를 입력하세요")

# 랜덤 글자 선택
rand_word = random.choice(str_list)
print("단어 선택 완료 게임을 시작합니다. 선택된 단어: ",rand_word)

# 블라인드 처리
length = len(rand_word)  # 선택된 단어의 길이를 계산하여 변수 length에 저장
blind_count = (length // 2) + (length % 2)  # 단어의 길이를 반으로 나누고, 나머지를 더해 올림하여 블라인드 처리할 글자의 개수를 계산
blind_word_list = list(rand_word)  # 선택된 단어를 문자 리스트로 변환하여 blind_word_list에 저장
blind_indices = []  # 블라인드 처리할 글자의 인덱스를 저장할 빈 리스트를 생성

# 블라인드 처리할 인덱스를 무작위로 선택하여 블라인드 처리
while len(blind_indices) < blind_count:
    index = random.randint(0, length - 1)  # 단어의 인덱스 범위 내에서 무작위 인덱스를 생성
    dup_found = False  # 중복된 인덱스가 발견되었는지 여부를 저장하는 변수
    for i in range(len(blind_indices)):  # 기존의 블라인드 처리된 인덱스와 무작위 인덱스를 비교
        if blind_indices[i] == index:  # 이미 블라인드 처리된 인덱스인 경우
            dup_found = True  # 중복된 인덱스가 발견되었음을 표시
            break
    if not dup_found:  # 중복되지 않은 경우
        blind_indices.append(index)  # 블라인드 처리할 인덱스를 리스트에 추가
        blind_word_list[index] = '_'  # 해당 인덱스의 문자를 블라인드 처리 

# 리스트를 문자열로 변환 #hi
blind_word = ""
i = 0

while i < len(blind_word_list):  # 블라인드 처리된 단어 리스트를 문자열로 변환
    blind_word += blind_word_list[i]  # 각 문자를 빈 문자열에 추가하여 결합
    i += 1
print("단어 :", blind_word)  # 블라인드 처리된 단어를 출력합니다.

correct_word = list(rand_word)  # 정답 단어를 문자 리스트로 변환하여 correct_word에 저장
guessed_word = list(blind_word)  # 사용자가 추측한 단어의 현재 상태를 문자 리스트로 변환하여 guessed_word에 저장
try_count = 1  # 시도 횟수를 저장하는 변수를 초기화

# 블라인드 처리된 글자 맞추기
while True:
    guess = input(f"{try_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개를 입력하세요.")  # 사용자가 추측한 글자를 입력
    found = False  # 추측한 글자가 단어에 있는지 여부를 저장하는 변수
    for index in blind_indices:  # 블라인드 처리된 인덱스를 순회하며
        if correct_word[index] == guess and guessed_word[index] == '_':  # 추측한 글자가 맞고 해당 위치가 블라인드 처리된 경우
            guessed_word[index] = guess  # 해당 위치의 블라인드 문자를 맞춘 글자로 교체
            found = True  # 추측한 글자가 단어에 있음을 표시
            break

    # 현재 상태 출력
    if found:  # 맞춘 글자가 있는 경우
        current_guess = ""
        i = 0
        while i < len(guessed_word):  # 현재 상태를 문자열로 변환
            current_guess += guessed_word[i]
            i += 1

        print("현재 상태", current_guess)  # 현재 상태를 출력
        if guessed_word == correct_word:  # 모든 글자를 맞춘 경우
            break  # 게임을 종료
    try_count += 1  # 시도 횟수를 증가

print("Clear - 선택된 단어: ", rand_word, "총 시도 횟수: ", try_count)  # 정답 단어와 총 시도 횟수를 출력
