import requests
import bs4 as BS

url = 'https://valuta.kg/'


def parseCurrencies():
    req = requests.get(url)
    html = BS.BeautifulSoup(req.content, 'lxml')
    currency_rows = html.find_all(class_='kurs-table')[1].find_all('tr')[1:]

    for row in currency_rows:
        currency_name = row.find_all('td')[0].text.strip()
        currency_rate = row.find_all('td')[2].text.strip()
        print(f'{currency_name}: {currency_rate}')


parseCurrencies()
