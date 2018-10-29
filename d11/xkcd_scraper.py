import requests
import bs4
from d11.pobieracz import pobierz

strona = 'https://xkcd.com/'

i = 0
for i in range(10):
    response = requests.get(strona)

    if response.status_code == 200:
        with open('kolejna_strona.html', 'w') as plik:
            plik.write(response.text)

        zupa = bs4.BeautifulSoup(response.text, "html.parser")

        kluska = zupa.select_one('div #comic img')
        zdjecie = kluska['src']

        sciezka = 'zdjecie' + str(i) + '.png'

        pobierz(zdjecie, sciezka)

        buttons_prev = zupa.select('.comicNav li a["rel=prev"]')

        links = None
        for el in buttons_prev:
            links.append(el['href'])

        link_id = links.pop(0).strip()
        strona = strona.strip() + link_id

        i += 1
    else:
        exit(404)