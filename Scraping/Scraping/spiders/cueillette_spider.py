import scrapy
import re

class MaisonsSpider(scrapy.Spider):
    
    #Nom du spider
    name = "scrapeMaisons"
    
    #Liste des URL à Scraper
    start_urls = [
        "https://duproprio.com/fr/quebec-rive-sud/levis/maison-en-rangee-de-ville-a-vendre/hab-5897-rue-berlioz-920663"]
        
        # Pour faire toutes les villes, essayer ça (à 25:06): 
        # https://youtu.be/lNajD34Sfmg
        

    #Parser
    def parse(self, response):
        
        #Nom du fichier texte
        filename = 'maisons.csv'
        
        #Extraction de l'adresse, prix et surface
        try:
            adresse = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div/h1/text()').extract()
            adresse = str(adresse)
            adresse = adresse.replace('[\'', '').replace(',', '').replace('\']', '')
        except:
            adresse = "Failed to parse"

        try:
            prix = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/text()').extract()
            prix = str(prix)
            prix = prix.replace('\\xa0', '')
            prix = re.search("\\d+\\$", prix, re.MULTILINE).group()
        except:
            prix = "Failed to parse"

        try:
            surface = response.xpath('/html/body/main/div[1]/div/div[1]/section[1]/article/div[1]/div[4]/div[1]/div[2]/span[2]/text()').extract()
            surface = str(surface)
            surface = re.search("\\d*\\s?\\d*\\s?\\d+\\spi", surface, re.MULTILINE).group()
            surface = surface.replace(' ', '') + "2"
        except:
            surface = "Failed to parse"
        
        #Création d'une ligne type csv
        line = {"adresse":adresse, "prix":prix, "surface":surface}

        #Ajout de la ligne au fichier
        with open(filename, "w") as f:
        
            fieldnames = ['adresse', 'prix', 'prix']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    
            writer.writerrow(line)
    
