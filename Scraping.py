import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://books.toscrape.com/'
book_data_list = []
page_number = 1
book_id = 1

while True:
    url = f'{base_url}catalogue/page-{page_number}.html'
    print(f"Scraping page {page_number}: {url}")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    allbooks = soup.find_all('article', class_='product_pod')

    for book in allbooks:
        title = book.h3.a["title"]  # Récupère le titre du livre
        price = book.find('p', class_='price_color').text.strip().replace('£', '') # Récupère le prix du livre
        availability = book.find('p', class_='instock availability').text.strip() # Récupère le status du livre
        rating_class = book.find('p', class_='star-rating')['class'][1]  # Extrait la classe qui indique le rating
        rating = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}.get(rating_class, 0)  # Récupère le nombre d'étoiles
        
        book_data_list.append({
            "ID": book_id,
            "Book Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })
        book_id += 1
    
    # Vérifier s'il y a une page suivante
    next_button = soup.find('li', class_='next')
    if next_button:
        page_number += 1
    else:
        print("No more pages found. Exiting...")
        break

# Convertir la liste en un DataFrame pandas
df = pd.DataFrame(book_data_list)

# Sauvegarder dans un fichier CSV
df.to_csv("book_list.csv", index=False)
