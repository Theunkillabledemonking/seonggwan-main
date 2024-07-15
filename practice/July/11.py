import os

# 스크립트의 위치를 기준으로 파일 경로 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'test.txt')

# 파일 열기 (읽기 및 쓰기 모드)
try:
    with open(file_path, "w+", encoding="utf-8") as f_handler:
    # 파일에서 모든 내용을 읽어 문자열로 저장
        msg = f_handler.read()
    
    # 읽은 문자열에서 "hello world" 문자열 추가
        msg += "hello world"
        
        # 변경된 문자열을 파일에 다시 쓰기
        f_handler.seek(0) # 파일의 포인터를 파일의 처음으로 이동
        f_handler.write(msg)
        f_handler.truncate() # 파일의 끝을 현재위치로 설정
        
        # 파일을 닫기
        f_handler.close()
        
        print("파일을 성공적으로 수정했습니다.")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다. {file_path}")