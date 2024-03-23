import requests
from bs4 import BeautifulSoup
class Douban:
    def __init__(self):
        self.URL = "https://movie.douban.com/top250"
        self.headnum = []
        for num_i in range(0, 251, 25):
            self.headnum.append(num_i)
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    def get_top250(self):
        for start in self.headnum:
            start = str(start)
            html = requests.get(self.URL, params={'start': start}, headers=self.header)
            soup = BeautifulSoup(html.text, "html.parser")
            name = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            for name_i in name:
                print(name_i.get_text())

if __name__ == "__main__":
    db = Douban()
    db.get_top250()