#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import calendar
import json
import collections
random.seed(int(time.time() * 1000))
ingredientes = []
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
    semanaComidas.append(comidas["comidas"][randComidas[i]])
    semanaCenas.append(comidas["cenas"][randCenas[i]])

print('<!DOCTYPE html>\n<html>\n<head>\n\t<link rel="stylesheet" href="style.css">\n\t<meta charset="UTF-8">\n</head>\n<body>')
print("\t<table>")
print('\t\t<tr id="cabecera"><th>Día</th><th>Comida</th><th>Cena</th></tr>')
for i in range(weekDays):
    print('\t\t<tr id="cuerpo"><th>' + calendar.day_name[i] + '</th><th>' + semanaComidas[i]["nombre"] + '</th><th>' + semanaCenas[i]["nombre"] + '</th></tr>')
print('\t</table>')

for i in semanaComidas:
    ingredientes.extend(i["ingredientes"])

for i in semanaCenas:
    ingredientes.extend(i["ingredientes"])

ingredientes = collections.Counter(ingredientes)

print("\t<br><br>***LISTA DE LA COMPRA***")
print("\t<ul>")
for ing, num in ingredientes.items():
    print("\t\t<li>" + str(num) + "x " + ing + "</li>")
print("\t</ul>")

# salida = salida.replace('Counter({', '')
# print(salida.replace('})', ''))

print('</body>\n</html>')
