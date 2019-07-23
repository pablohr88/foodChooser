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

randComidas = list(random.sample(range(0, len(comidas["comidas"])), weekDays))
semanaComidas = []
randCenas = list(random.sample(range(0, len(comidas["cenas"])), weekDays))
semanaCenas = []

for i in range(weekDays):
    semanaComidas.append(comidas["comidas"][randComidas[i]])
    semanaCenas.append(comidas["cenas"][randCenas[i]])

print('From: pablohr88@gmail.com\nMIME-Version: 1.0\nContent-Type: text/html\nSubject: Menú semanal <3\n\n')

print('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n\t<link rel="stylesheet" href="style.css">\n\t<meta charset="UTF-8">\n\t<style>\n\ttable, th, td {border-style: solid; border-width: 2px}\n\t#cabecera{font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; text-transform: uppercase; color: darkslategray; text-align: center}\n\t#cuerpo{font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; font-weight: 50; text-align: left}\n\t</style></head>\n<body>')
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
