import requests
import unidecode
from bs4 import BeautifulSoup


ROOT_URL = 'https://www.climatempo.com.br/'

def getState(state):
    headers = { 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': ROOT_URL }
    payload = { 'uf' : state }

    r = requests.post('https://www.climatempo.com.br/json/busca-cidades-uf', data=payload, headers=headers)

    if r.status_code == 200:
        return r

    return None

def processCity(state, cityObj):
    urlSeq = [ROOT_URL, 'climatologia/', str(cityObj['idcity']), '/', clean(cityObj['city']), '-', state.lower()]
    url = ''.join(urlSeq)
    print('Processing ', url)
    return process(cityObj['city'], state, url)

def process(city, state, url):
    response = []
    r = requests.get(url)

    if r.status_code == 200:
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        if soup is not None:
            table = soup.findAll('table', { 'role': 'grid'})
            if table is not None:
                for tr in table[0].findAll('tr'):
                    if tr.td is not None:
                        tds = tr.findAll('td')
                        response.append({ 'city': city, 'state': state, 'month': tds[0].string, 'minTemp': tds[1].string, 'maxTemp': tds[2].string, 'precipitation': tds[3].string })
    return response

def clean(str):
    return unidecode.unidecode(str).replace(' ', '').lower()