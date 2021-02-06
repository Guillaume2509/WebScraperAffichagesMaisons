import pandas as pd
from scrapy.crawler import CrawlerProcess
from Scraping.Scraping.spiders.spiderMaisons import MaisonsSpider


#TODO: 1-Scraping 2-Scoring

def Scraping():
    '''Appeler le Scraping'''
    #Tutoriel: https://towardsdatascience.com/how-to-run-scrapy-from-a-script-ff07fd6b792b
    
    #Ici on veut starter le crawler à même le script python, ainsi on fait:
    #1) On importe l'objet CrawlerProcess(), qui englobe le module Twister de Python
    process = CrawlerProcess()
    
    #2) On configure l'objet CrawlerProcess à notre spider MaisonSpider
    process = process.crawl(scrapeListeAffichagesDuProprio)
    
    #3) On démarre le Crawler, comme si on était sur la ligne de commande. Il devrait nous retourner notre fichier CSV au Scraping/maisons.csv
    process.start()
    
def Scoring():
    '''Construire le Scoring'''
    
    #Loader le csv
    maisons = pd.read_csv("Scraping/maisons.csv", args)
    
def display():
    '''Print the results'''
    read_csv(mettre le path du csv ici)
            

if __name__ == "__main__":
    Scraping()
    #TODO: Faire fonctionner le debugger dans VSCode x
    
    Scoring()
    
