# Varianta Secvențială
Acest proiect demonstrează procesul de extragere a datelor despre produse de pe un site de comerț electronic, analiza acestora și vizualizarea rezultatelor. Se concentrează pe extragerea datelor din secțiunea de telefoane mobile a site-ului eMAG, obținând titluri și prețuri de produse, scrierea datelor într-un fișier CSV, efectuarea unei analize statistice și generarea unui grafic cu bare care prezintă cele mai scumpe 10 produse.

# Caracteristici
1. Scraping Web: Utilizează biblioteca BeautifulSoup din Python pentru a extrage date despre produse din mai multe pagini ale site-ului eMAG. 
2. Procesare Secvențială: Implementează un algoritm secvențial pentru a parcurge fiecare pagină a site-ului și a extrage datele în mod secvențial. 
3. Export de Date: Salvează datele extrase într-un fișier CSV folosind modulul CSV încorporat. 
4. Analiză a Datelor: Calculează prețurile medii, minime și maxime ale produselor extrase. 
5. Vizualizare a Datelor: Generează un grafic cu bare al celor mai scumpe 10 produse folosind biblioteca Matplotlib.

# Functionalitate
1. Scraping: Funcția scrape_website extrage și analizează conținutul HTML de pe fiecare pagină a listei de produse de pe site-ul eMAG, parcurgându-le secvențial. 
2. Procesare Secvențială: Paginile sunt scrapate într-un mod secvențial, fără utilizarea procesării paralele, ceea ce înseamnă că fiecare pagină este procesată înainte de a trece la următoarea. 
3. Stocare a Datelor: Datele extrase sunt colectate într-o listă de dicționare și scrise într-un fișier CSV folosind modulul CSV din Python. 
4. Analiză Statistică: Calculează și afișează prețurile medii, minime și maxime ale produselor colectate. 
5. Vizualizare: Generează și salvează un grafic cu bare al celor mai scumpe 10 produse folosind biblioteca Matplotlib.

# Rezultat
Programul afișează următoarele în consolă:
1. Timpul total de execuție 
2. Numărul de produse extrase 
3. Prețurile medii, minime și maxime
   
Total execution time: 1.62 seconds
Number of products extracted: 60
Average price: 2876.27
Minimum price: 109.99
Maximum price: 7299.99

Se generează totodata:
1. scraped_data.csv: Un fișier CSV care conține numele și prețurile tuturor produselor extrase. 
2. chart10.png: O imagine a unui grafic cu cele mai scumpe 10 produse.
