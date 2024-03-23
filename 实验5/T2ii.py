import requests
from bs4 import BeautifulSoup

class Tianqi:
    def __init__(self):
        self.URL = "https://www.tianqi.com/hangzhou/30"

        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    def getwather(self):
        html = requests.get(self.URL,headers=self.header)
        soup = BeautifulSoup(html.text,"html.parser")#
        daydate = soup.select('body > div.w1100.newday40_top > div.inleft > ul.weaul > li > a > div.weaul_q.weaul_q > span.fl')
        weatherdate = soup.select('body > div.w1100.newday40_top > div.inleft > ul.weaul > li > a > div:nth-child(3)')
        for i in range(0, 30):
            print(daydate[i].get_text(), " ", weatherdate[i].get_text())

if __name__ == "__main__":
    tq=Tianqi()
    tq.getwather()
