#  Web Scraping des livres avec Python  

##  Objectif  
Ce projet est une **introduction au web scraping** avec **Python**. L'objectif principal était d'extraire des données structurées sur les livres du site [Books to Scrape](http://books.toscrape.com/) et de les stocker dans un fichier **CSV**, prêt à être exploité pour une analyse dans Power BI. 

##  Structure du site web  

Avant d'extraire les données, j'ai analysé le site web et son code HTML. Voici une capture d'écran pour montrer où se trouvent une des informations :  

![Structure du site](https://github.com/sbocquetpro/Web-Scraping/blob/main/Scraping%20Screenshot.png) 

On récupère les informations en sélectionnant les balises suivantes :  
- **Titre** → `<h3> <a title="Book Title">`  
- **Prix** → `<p class="price_color">`  
- **Disponibilité** → `<p class="instock availability">`  
- **Note** → `<p class="star-rating">` (exploité via la classe CSS)  

Ensuite, on utilise **BeautifulSoup** pour extraire ces balises et récupérer les valeurs.  


##  Données extraites  
Pour chaque livre, les informations suivantes ont été récupérées :  
- **Titre** 📖  
- **Prix (£)** 💰  
- **Disponibilité** 📦  
- **Note (étoiles)** ⭐  

Ces données peuvent être utilisées pour analyser la distribution des prix, la relation entre les notes et les prix, ou encore la disponibilité des livres sur le marché.  

##  Technologies utilisées  
- **Python** 
- **Requests** → Récupération des pages web  
- **BeautifulSoup** → Extraction des données HTML  
- **Pandas** → Stockage et export des données  

##  Fonctionnalités du script  
✅ Extraction des données de toutes les pages du site  
✅ Nettoyage et structuration des données  
✅ Stockage des informations dans un **fichier CSV**  
✅ Prêt pour une analyse approfondie sous **Power BI**  

## Possibilités d'analyse avec Power BI  
Une fois les données extraites, elles peuvent être visualisées sous Power BI pour répondre à plusieurs questions :  
- **Quels sont les prix moyens des livres ?**  
- **Existe-t-il une corrélation entre la note et le prix ?**   
- **Quelle est la répartition des stocks disponibles ?**   

##  Exécution du script  

pip install requests beautifulsoup4 pandas
