import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# lxml 파서를 이용해 객체 생성
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  # 첫번째로 발견되는 태그
# print(soup.a.attrs) # a element의 속성 정보
# print(soup.a["href"]) # a element의 href 속성 값 정보

# print(soup.find('a', attrs={"class": "Nbtn_upload"})) #find() 함수
# print(soup.find(attrs={"class": "Nbtn_upload"}))  # find() 함수

# print(soup.find('li', attrs={"class": "rank01"}))
# rank1 = soup.find('li', attrs={"class": "rank01"})
# print(rank1.a.get_text())
# # print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling  # 다음 위치 element
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)

# print(rank1.find_next_sibling('li').a.get_text())
# rank1.find_next_siblings('li') # 다음 형제들 모두 가져옴

webtoon = soup.find('a', text='연애혁명-338. 혼선 (1)')
print(webtoon)
