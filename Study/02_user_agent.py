import requests
url = "https://umku10.tistory.com/6"
# headers에 user agent 정의
# user agent는 what is my user agent 검색
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

print(len(res.text))
