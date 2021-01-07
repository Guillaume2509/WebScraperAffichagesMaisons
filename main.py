from scrapy.crawler import CrawlerProcess
from Scraping.Scraping.spiders.cueillette_spider import MaisonsSpider


#TODO: 1-Scraping 2-Scoring

def Scraping():
    '''Appeler le Scraping'''
    process = CrawlerProcess()
    
    process = process.crawl(MaisonsSpider)
    
def Scoring():
    '''Construire le Scoring'''
    import json
    
    with open('Scraping/maisons.csv', 'wb') as f:

    return "Todo"
            

if __name__ == "__main__":
    Scraping()
    
    Scoring()
    