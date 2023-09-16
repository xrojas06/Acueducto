import dir
import scrapping as sp
import nlp
from shapely.geometry import Polygon, Point
import numpy as np
import matplotlib.pyplot as plt

url = 'https://www.acueducto.com.co/wps/portal/EAB2/Home/atencion-al-usuario/programacion_cortes'
api_key = 'AIzaSyDbvqxCdq01VBGy1YftdU37CFd69rj0mI0'

direction = "Cra. 7 #33-43, Bogotá"
lugar, barrio = sp.scrap_information(url)
direcciones = nlp.busqueda(lugar)
points = np.array([])

for i in direcciones:
    if len(direcciones[i]):
        for nums in direcciones[i]:
            temp = i + ' ' + nums  +', Bogotá'
            coords = dir.geocode_direction(temp, api_key)
            points = np.append(points, coords)

points = np.reshape(points, (-1, 2)).tolist()
points = sorted(points, key=lambda coord: (coord[1], coord[0]))
point_to_check = Point(dir.geocode_direction(direction, api_key))

polygon = Polygon(points)

is_inside = polygon.contains(point_to_check)

# Imprimir el resultado
print(f'¿El punto está dentro del polígono?: {is_inside}')




x, y = polygon.exterior.xy

plt.figure()
plt.plot(x, y, color='blue', alpha=0.7,
         linewidth=3, solid_capstyle='round', zorder=2)
plt.fill(x, y, alpha=0.3, closed=True, edgecolor='none', zorder=1)

punto_x, punto_y = point_to_check.x, point_to_check.y
plt.plot(punto_x, punto_y, 'ro', label='Punto')

plt.xlabel('Latitud')
plt.ylabel('Longitud')
plt.title('Polígono y Punto')
plt.legend()
plt.show()
