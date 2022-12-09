import requests
from bs4 import BeautifulSoup

# Envie uma solicitação para a página da web
response = requests.get('http://www.example.com')

# Analise o conteúdo da página com o BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extraia os dados desejados
data = soup.find('div', attrs={'class': 'data'})

# Imprima os dados extraídos
print(data)
