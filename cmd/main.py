import requests 

URL_1 = 'https://www.wikipedia.org/'
URL_2 = 'https://www.python.org/'

def main():
    req = requests.get(URL_1, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    })
    if req.status_code == 200:
        print(req.headers)
        with open('req.html', 'wb') as f:
            f.write(req.content)

    else:
        print(f'Ошибка запроса\nStatuse Code: {req.status_code}')
        with open('error.html', 'wb') as f:
            f.write(req.content)

if __name__ == '__main__':
    main()