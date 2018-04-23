'''

LV1. 문자열 다루기 기본

alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.

s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.

예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다

'''


# 내 풀이
def alpha_string46(s):
    if s.isdigit() and len(s) in [4, 6]:
        return True
    else:
        return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(alpha_string46("a234"))
print(alpha_string46("1234"))
print(alpha_string46('043n'))


# 짧은 풀이
def alpha_string46(s):
    return  s.isdigit() and len(s) in [4, 6]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(alpha_string46("a234"))
print(alpha_string46("1234"))
print(alpha_string46('043n'))
