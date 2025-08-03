import requests
from bs4 import BeautifulSoup

BASE_URL = "https://rostender.info/extsearch"

def parse_tenders(max_tenders=100):
    tenders = []
    page = 1

    while len(tenders) < max_tenders:
        url = f'{BASE_URL}?page={page}'
        try:
            res = requests.get(url)
        except requests.exceptions.RequestException as e:
            return f'Ошибка {e}'

        soup = BeautifulSoup(res.content, 'lxml')
        table = soup.find(id="table-constructor")
        if not table:
            break

        data = table.find(id='table-constructor-body').find_all('article')
        if not data:
            break

        for card in data:
            tender = {
                'number': card.find('span', {'class': 'tender__number'}).text.strip().split('№')[-1],
                'title': card.find('div', attrs={'class': 'tender-info'}).text.strip(),
                'url': f'https://rostender.info{card.find('div', attrs={'class': 'tender-info'}).find('a').get('href')}',
                'end_date': card.find('span', attrs={'class': 'tender__countdown-text'}).text.strip().split()[2:],
                'address': [card.find('div', attrs={'class': 'tender-address'}).text.strip(),
                            card.find('a', attrs={'class': 'tender__region-link'}).text.strip()],
                'starting_price': card.find('div', attrs={'class': 'starting-price'}).text.strip().split('\n')[-1],
                'sectors': [c.text.strip() for c in
                            card.find('div', attrs={'class': 'tender-customer-branches'}).find_all('li', attrs={
                                'class': 'list-branches__li'})]
            }

            tenders.append(tender)

            if len(tenders) >= max_tenders:
                break
        page += 1

    return tenders

