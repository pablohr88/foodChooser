#!/usr/bin/env python3
# -*- coding: windows-1252 -*-

import smtplib

EMAIL_USER = "menu.semanal.phr@gmail.com"
EMAIL_PWD = "menu.semanal"

destinatarios = ["albacp89@gmail.com, pablohr88@gmail.com",
                 "stellapadillasanchez@yahoo.es",
                 "maui_maui89@gmail.com, maribum2001@yahoo.com"]

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(EMAIL_USER, EMAIL_PWD)
for destEmail in destinatarios:
  
  server.sendmail(EMAIL_USER,
                  destEmail,
                  )
server.quit()