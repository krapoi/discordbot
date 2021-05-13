import requests
from bs4 import BeautifulSoup as bs
import lxml

class krapoi():
    url = "http://ncov.mohw.go.kr/"
    result = []

    def __init__(self):
        pass

    def requestRun(self) :
        response = requests.get(self.url)
        responseCode = int(response.status_code)

        if (responseCode == 200):
            soup = bs(response.content, 'lxml')
        else:
            return False

        today = soup.find("div", {"class": "liveNum_today_new"}).findAll("span", {"class": "data"})
        today_domestic = int(today[0].text)  # 리스트 첫 번째 요소 (국내발생)
        today_overseas = int(today[1].text) # 리스트 두 번째 요소 (해외유입)
        accumulate_confirmed = soup.find("div", {"class": "liveNum"}).find("span", {"class": "num"}).text[4:]  # 앞에 (누적) 글자 자르기
        self.result.append({
            'today_domestic': today_domestic,
            'today_overseas': today_overseas,
            'accumulate_confirmed': accumulate_confirmed
        })
        return True
    
    def requestReturn(self):
        if self.result:
            return self.result[-1]
        else:
            return None

