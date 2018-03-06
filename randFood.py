#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import calendar
import json
random.seed(int(time.time() * 1000))
comidas = json.load(open("comidas.json", encoding='utf-8'))
# cenas=json.load(open("cenas.json", encoding='utf-8'))
# print(comidas)
# print("\n\n")
# for i in comidas["comidas"]:
#  print(i["nombre"])

# cenas = ["Gallos", "Judías verdes", "Tosta salmón", "Torta cerdo queso", "Esfera salmón aguacate", "Tortilla patata", "Tortilla de ...", "Acelgas", "Espinacas", "Pencas", "Croquetas", "Alitas", "Embutido"]
# semanaComida = list(random.sample(range(0,len(comidas["comidas"])), 5))
# semanaCena = list(random.sample(range(0,len(cenas["cenas"])), 5))

randComidas = list(random.sample(range(0, len(comidas["comidas"])), 5))
semanaComidas = []
# randCenas = list(random.sample(range(0,len(cenas["cenas"])), 5))

for i in range(5):
    semanaComidas[i] = list(comidas["comidas"][randComidas[i]]["nombre"])

print('<!DOCTYPE html>\n<html>\n<head>\n\t<link rel="stylesheet" href="style.css">\n\t<meta charset="UTF-8">\n</head>\n<body>')
print("<table>")
print('<tr id="cabecera"><th>Día</th><th>Comida</th><th>Cena</th></tr>')
for i in range(5):
    print('<tr id="cuerpo"><th>' +
          calendar.day_name[i] + '</th><th>' + semanaComidas[i] + '</th></tr>')
    # print('<tr id="cuerpo"><th>'+calendar.day_name[i]+'</th><th>'+cenas["cenas"][semanaCenas[i]]["nombre"]+'</th></tr>')
print('</table>')
print('</body>\n</html>')
