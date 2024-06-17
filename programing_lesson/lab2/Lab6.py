# 태그 이름과 내용을 매겨변수를 받고
# 해탕 태그로 감싸진 HTMl 요소를 반환하는 함수

def wrap_in_tag(Code, str):
    msg = (f"<{Code}>{str}</{Code}>")
    return msg

print(wrap_in_tag('p', 'hello'))
print(wrap_in_tag('b', 'world'))