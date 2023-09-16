import requests
from bs4 import BeautifulSoup
import dateparser

url = 'https://www.acueducto.com.co/wps/portal/EAB2/Home/atencion-al-usuario/programacion_cortes'


def scrap_information(url):
    response = requests.get(url)
    if response.status_code == 200:
    # Parsea el contenido HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

    # Encuentra los elementos HTML que contienen la información de los cortes de agua
    # y extrae la información que necesitas
    # Esto dependerá de la estructura específica de la página web.

        tabla_cortes_agua = soup.find('table', {
        'class': 'table table-striped mt20 table-bordered table-blue w100 table-responsive'})
    # Por ejemplo, si la información se encuentra en elementos div con una clase específica:
        if tabla_cortes_agua:
            files = tabla_cortes_agua.find_all("tr")
            dates_cortes = {}
            for file in files[1:]:
            # Encuentra todas las celdas de la fila
                cells = file.find_all("td")

                if len(cells) == 1:
                    date = cells[0].text.strip()
                    object_date = dateparser.parse(date, languages=['es'])
                    dates_cortes[object_date.date()] = {}

                if len(cells) >= 2:
                # La tercera celda contiene la información del lugar
                    barrio = cells[1].text.strip()
                    lugar = cells[2].text.strip()
                    print("Lugar del corte de agua:", lugar)
                    print("Barrio del corte de agua:", barrio)
                    return lugar, barrio

        else:
            print("No se encontró la tabla de cortes de agua.")
    else:
        print("Error al obtener la página:", response.status_code)
