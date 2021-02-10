import requests
from bs4 import BeautifulSoup

# url + query
url = 'https://search.shopping.naver.com/search/all?query=' + \
    '주차번호판'+'&cat_id=&frm=NVSHATC'
res = requests.get(url)
res.raise_for_status()  # 에러시 종료

soup = BeautifulSoup(res.text, "lxml")
add_lst = soup.find_all('button', attrs={'class': 'ad_ad_stk__12U34'})
cnt = 0
for rank in add_lst:
    if cnt == 10:
        break
    par = rank.parent.parent.parent
    mall = par.find('div', attrs={'class': 'basicList_mall_title__3MWFY'})
    print(mall.a.get_text())
    cnt += 1
