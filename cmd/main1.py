import requests 
from bs4 import BeautifulSoup
import time

URL_1 = 'https://habr.com/ru/feed/'
URL_2 = 'https://www.python.org/'

def parse_article(article):
    header = article.find("h2", class_= "tm.title")

    if header == None:
        raise ValueError('Article do not have header. SKIP...')

    header_text = header.find('span').text
    article_link = header.find('a').atts['href']
    article_views = article.find('span', class_= "tm-icon-counter__value" ).text
    # article_tags = list(map(lambda tag: tag.find('span').text, article.find('div',  class_="tm-publications-hubs")))
    return {'header_text': header_text, 'article_link': article_link, 'article_views': article_views, 'article_tags': article_tags}

def main():
    req = requests.get(URL_1, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    })
    if req.status_code == 200:
        soup = BeautifulSoup(req.content, 'html.parser')

        lang_list = soup.find_all('a', class_='link-box')

        parsed_articles = []
            
        for a in articles_list:
            try:
                parsed_articles.append(parse_article(a))
            except:
                print(e)
        print(parsed_articles)

     results_path = check_and_create_result()
            
        with open(f'{result_path}/habr-result-{time.time()}.txt', 'a', encoding='utf-8') as f:
            for a in parsed_articles:
                f.write(f'header': {a['header_text']}\nviews: {a['articles_views']}\nlink: https://habr.com/ru/feed/)

    else:
        print(f'Ошибка запроса\nStatuse Code: {req.status_code}')




if __name__ == '__main__':
    main()  