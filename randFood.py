#!/usr/bin/env python3
# -*- coding: windows-1252 -*-

import time
import random
import calendar
import json
import collections
import sys

random.seed(int(time.time() * 1000))
weekDays = 5
comidas = json.load(open("comidas.json", encoding='windows-1252'))

ingredientes = []
randComidas = list(random.sample(range(0, len(comidas["comidas"])), weekDays))
semanaComidas = []
randCenas = list(random.sample(range(0, len(comidas["cenas"])), weekDays))
semanaCenas = []

for i in range(weekDays):
    semanaComidas.append(comidas["comidas"][randComidas[i]])
    semanaCenas.append(comidas["cenas"][randCenas[i]])

original_stdout = sys.stdout
with open("menu.html", "w", encoding='windows-1252') as file:
    sys.stdout = file

    print('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//ES" \
        "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n\t<link \
        rel="stylesheet" href="style.css">\n\t<meta charset="WINDOWS-1252">\n\t\
        </head>\n<body>')
    print("\t<table>")
    print('\t\t<tr id="cabecera"><th>Dí­a</th><th>Comida</th><th>Cena</th></tr>')
    for i in range(weekDays):
        print('\t\t<tr id="cuerpo"><th>' + calendar.day_name[i] + '</th><th>' +\
            semanaComidas[i]["nombre"] + '</th><th>' + semanaCenas[i]["nombre"] +\
            '</th></tr>')
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

    print('</body>\n</html>')
    sys.stdout = original_stdout