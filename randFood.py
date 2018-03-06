#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import calendar
import json
random.seed(int(time.time() * 1000))

weekDays = 5
comidas = json.load(open("comidas.json", encoding='utf-8'))
# cenas=json.load(open("cenas.json", encoding='utf-8'))
# print(comidas)
# print("\n\n")
# for i in comidas["comidas"]:
#  print(i["nombre"])

# cenas = ["Gallos", "Judías verdes", "Tosta salmón", "Torta cerdo queso", "Esfera salmón aguacate", "Tortilla patata", "Tortilla de ...", "Acelgas", "Espinacas", "Pencas", "Croquetas", "Alitas", "Embutido"]
# semanaComida = list(random.sample(range(0,len(comidas["comidas"])), 5))
# semanaCena = list(random.sample(range(0,len(cenas["cenas"])), 5))

randComidas = list(random.sample(range(0, len(comidas["comidas"])), weekDays))
semanaComidas = []
randCenas = list(random.sample(range(0, len(comidas["cenas"])), weekDays))
semanaCenas = []
# randCenas = list(random.sample(range(0,len(cenas["cenas"])), 5))

for i in range(weekDays):
    semanaComidas.append(comidas["comidas"][randComidas[i]]["nombre"])
    semanaCenas.append(comidas["cenas"][randCenas[i]]["nombre"])

print('<!DOCTYPE html>\n<html>\n<head>\n\t<link rel="stylesheet" href="style.css">\n\t<meta charset="UTF-8">\n</head>\n<body>')
print("\t<table>")
print('\t\t<tr id="cabecera"><th>Día</th><th>Comida</th><th>Cena</th></tr>')
for i in range(weekDays):
    print('\t\t<tr id="cuerpo"><th>' + calendar.day_name[i] + '</th><th>' + semanaComidas[i] + '</th><th>' + semanaCenas[i] + '</th></tr>')
print('\t</table>')
print('</body>\n</html>')
