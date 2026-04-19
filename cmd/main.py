import requests 
from bs4 import BeautifulSoup
import os

URL_1 = 'https://www.wikipedia.org/'
URL_2 = 'https://www.python.org/'

def main():
    req = requests.get(URL_1, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    })
    if req.status_code == 200:
        print(req.headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        lang_list = soup.find_all('a', class_='link-box')

        result_path = '../results'
        if not os.path.exists(result_path):
            os.makedirs(result_path)
            
        with open('../result/wikipedia-results.txt', 'w', encoding='utf-8') as f:
            for element in lang_list:
                url = f"https:{element['href']}"
                lang = element.find('strong').text
                cnt = element.find('small').text
                print(lang, url, cnt)
                f.write(f'{url};{lang};{cnt}\n')

    else:
        print(f'Ошибка запроса\nStatuse Code: {req.status_code}')

if __name__ == '__main__':
    main()