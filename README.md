# Varianta Paralela
Acest proiect demonstrează procesul de extragere a datelor despre produse de pe un site de comerț electronic, analiza acestora și vizualizarea rezultatelor. Se concentrează pe extragerea datelor din secțiunea de telefoane mobile a site-ului eMAG, obținând titluri și prețuri de produse, scrierea datelor într-un fișier CSV, efectuarea unei analize statistice și generarea unui grafic cu bare care prezintă cele mai scumpe 10 produse.

# Caracteristici
1. Scraping Web: Utilizează biblioteca BeautifulSoup din Python pentru a extrage date despre produse din mai multe pagini ale site-ului eMAG. 
2. Procesare Paralelă: Implementează modulul concurrent.futures și ThreadPoolExecutor din Python pentru scrapare și procesare eficientă a datelor. 
3. Export de Date: Salvează datele extrase într-un fișier CSV folosind modulul CSV încorporat. 
4. Analiză a Datelor: Calculează prețurile medii, minime și maxime ale produselor extrase. 
5. Vizualizare a Datelor: Generează un grafic cu bare al celor mai scumpe 10 produse folosind biblioteca Matplotlib.

# Functionalitate
1. Scraping: Funcția scrape_website extrage și analizează conținutul HTML de pe fiecare pagină a listei de produse de pe site-ul eMAG. 
2. Procesare Paralelă: Paginile sunt scrapate în mod concurrent folosind ThreadPoolExecutor pentru procesare eficientă. 
3. Stocare a Datelor: Datele extrase sunt colectate într-o listă de dicționare și scrise într-un fișier CSV folosind modulul CSV din Python. 
4. Analiză Statistică: Calculează și afișează prețurile medii, minime și maxime ale produselor colectate. 
5. Vizualizare: Generează și salvează un grafic cu bare al celor mai scumpe 10 produse folosind biblioteca Matplotlib.

# Rezultat
Programul afișează următoarele în consolă:
1. Timpul total de execuție 
2. Numărul de produse extrase 
3. Prețurile medii, minime și maxime

Se generează totodata:
1. scraped_data.csv: Un fișier CSV care conține numele și prețurile tuturor produselor extrase. 
2. chart10.png: O imagine a unui grafic cu cele mai scumpe 10 produse.
