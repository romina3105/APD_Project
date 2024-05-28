# Web Scraping Secvential
Acest proiect realizează extragerea de date din mai multe site-uri web într-o manieră secvențială. Scopul principal este de a extrage informații despre produsele dintr-o anumită categorie de pe site-ul eMAG.

# Descriere
Proiectul folosește Python pentru a realiza web scraping-ul. Datele sunt extrase din mai multe pagini web ale unei categorii specifice de produse, în acest caz, telefoane mobile de pe eMAG. Informațiile extrase includ numele produselor și prețurile lor.

# Structura Proiectului
Proiectul este structurat în următoarele componente:

a) main.py: Fișierul principal al aplicației, care conține logica de coordonare a extragerii datelor și salvarea acestora în fișierele corespunzătoare.

b) web_scraper.py: Modul care conține funcția pentru extragerea datelor din paginile web folosind o abordare secvențială.

c) utilities.py: Modul care conține funcții de utilitate pentru efectuarea cererilor HTTP și analiza paginilor HTML.
