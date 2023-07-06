from bs4 import BeautifulSoup

import requests
#desisto tentei instalar a extensão mas deu ruim em

site = requests.get('https://www.climatempo.com.br/').content
# objeto site recebendo o conteúdo da requisição http do site

soup = BeautifulSoup(site, 'html.parser')
#o objeto soup baixando o html

print(soup.prettify())
#transforma html em string e o print vai exibir o html