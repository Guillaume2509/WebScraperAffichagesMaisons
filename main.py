from scrapy.crawler import CrawlerProcess
from Scraping.Scraping.spiders.cueillette_spider import MaisonsSpider


#TODO: 1-Scraping 2-Scoring

def Scraping():
    '''Appeler le Scraping'''
    #Tutoriel: https://towardsdatascience.com/how-to-run-scrapy-from-a-script-ff07fd6b792b
    process = CrawlerProcess()
    
    process = process.crawl(MaisonsSpider)
    
def Scoring():
    '''Construire le Scoring'''
    import json
    
    with open('Scraping/maisons.csv', 'wb') as f:

    return todo
    
def display():
    '''Print the results'''
    read_csv(mettre le path du csv ici)
            

if __name__ == "__main__":
    Scraping()
    
    Scoring()
    