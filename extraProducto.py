# https://www.youtube.com/watch?v=i4sHownM-KY
import requests
from bs4 import BeautifulSoup

url = 'https://listado.mercadolibre.com.ar/pc#D[A:pc]'

response = requests.get(url)

# Consultamos si el estado es 200 (o qeu sea correcto)
if response.status_code == 200:
    # Pasamos la respuesta a un objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    productos = soup.find_all('div', class_='ui-search')
    print(productos)
