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
    
    with open('dataFlips.csv', 'wb') as f:

    fieldnames = ['var1', 'var2', 'etc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerrow({'var1': 'gen1', 'var2': 'gen2', 'etc': 'genAutres'})
            

if __name__ == "__main__":
    Scraping()
    
    Scoring()
    