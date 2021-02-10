import re

p = re.compile('ca.e')
# . (ca.e)  : 하나의 문자 > case, care, ...
# ^ (^de)   : 문자열의 시작 > desk, destination, decade
# $ (se$)   : 문자열의 끝 > case, base ...


def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string:", m.string)  # 입력받은 문자열
        print("m.start():", m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작/끝 index
    else:
        print("not matched")


m = p.match('ss')
print_match(m)

m = p.search('good care')
print_match(m)

lst = p.findall('careless cafe')  # findall : 일치하는 모든 것을 리스트형태로 반환
print(lst)
