

import requests

url = 'https://www.adres.gov.co/consulte-su-eps'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)  # Esto imprimirá el contenido HTML de la página
else:
    print('Error al acceder a la página:', response.status_code)
