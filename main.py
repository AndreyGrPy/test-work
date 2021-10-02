import requests
from bs4 import BeautifulSoup
import json
import time


repository = []
while True:
    def get_sours_html():
        headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
                "Accept": "*/*"
            }
        url = "https://112ua.tv/"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        all_list = soup.find('div', id="tabs-top-news").find_all('li')

        for hot_news in all_list:

            try:
                times = hot_news.find('time').text
                href = hot_news.find('a').get('href')
                text = hot_news.find('a').text
            except:
                continue
            repository.append({

                'Category': times,
                'Href': href,
                'Text': text,
            })

        with open('hot_news_uk112.json', 'a') as file:
            json.dump(repository, file, indent=4, ensure_ascii=False)

    time.sleep(1)


    def main():
        get_sours_html()


    if __name__ == '__main__':
        main()