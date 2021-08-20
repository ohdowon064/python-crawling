# 1. 라이브러리 임포트
import requests
from bs4 import BeautifulSoup

# 2. 웹페이지 가져오기
res = requests.get('http://v.media.daum.net/v/20170615203441266')

# 3. 웹페이지 파싱하기
# content 안에 HTML 코드들이 들어있다.
soup = BeautifulSoup(res.content, 'html.parser')

# 4. 필요한 데이터 추출하기
mydata = soup.find('title')

# 5. 추출한 데이터 활용하기
print(mydata.get_text())