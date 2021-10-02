All libraries used for parsing::
""" Flask, Jinja2, MarkupSafe, Werkzeug, beautifulsoup4, bs4, certifi, charset-normalizer, click, idna, itsdangerous, lxml, pip, requests, setuptools, soupsieve, urllib3  """


Test work  'Beautiful Soup'  >> description of implementation


install library::

    import requests
    from bs4 import BeautifulSoup
    import json
    import time


create a repository where the data that we parsed will be stored::

    repository = []

we create a cycle for constant updating of the latest news::

    while True:


create our function to collect data from the site::

    def get_sours_html():
        headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
                "Accept": "*/*"
            }
the site, from which we will parse the top news::

        url = "https://112ua.tv/"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        all_list = soup.find('div', id="tabs-top-news").find_all('li')


extracting all the <<URLs, time,texts>> found within a page's tags::

        for hot_news in all_list:

            try:
                times = hot_news.find('time').text
                href = hot_news.find('a').get('href')
                text = hot_news.find('a').text
            except:
                continue
we fill our specially prepared repository with data. which were taken from the site::

            repository.append({

                'Category': times,
                'Href': href,
                'Text': text,
            })


create a 'json' file from our repository::

        with open('hot_news_uk112.json', 'a') as file:
              json.dump(repository, file, indent=4, ensure_ascii=False)

time after which our ""while""" collects current news from the site::
(time is indicated in minutes)

    time.sleep(1)

Run parsing::
(wait up to 30 sec)

        def main():
            get_sours_html()


    if __name__ == '__main__':
        main()







