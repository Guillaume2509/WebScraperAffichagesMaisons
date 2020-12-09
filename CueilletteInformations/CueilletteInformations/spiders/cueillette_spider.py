import scrapy
import re

class MaisonsSpider(scrapy.Spider):
    
    #Nom du spider
    name = "AffichageMaisons"
    
    #Liste des URL à Scraper
    start_urls = [
        "https://duproprio.com/fr/quebec-rive-sud/levis/maison-a-vendre/hab-5338-rue-saint-georges-744976#la-capitale"]
        

    #Parser
    def parse(self, response):
        
        #Nom du fichier texte
        filename = 'maisons.txt'
        
        #Extraction de l'adresse, prix et surface
        adresse = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div/h1/text()').extract()
        prix = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/text()').extract()
        prix = str(prix)
        prix = prix.replace('\\xa0', '')
        prix = re.search("\\d+\\$", prix, re.MULTILINE).group()
        surface = response.xpath('/html/body/main/div[1]/div/div[1]/section[1]/article/div[1]/div[4]/div[1]/div[2]/span[2]/text()').extract()
        
        #Création d'une ligne type csv
        #line = str(adresse) + "," + prix + "," + str(surface)
        line = prix

        #Ajout de la ligne au fichier
        with open(filename, "w") as f:
            f.write(line)
