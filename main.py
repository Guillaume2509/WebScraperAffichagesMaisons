from scrapy.crawler import CrawlerProcess
from Scraping.Scraping.spiders.cueillette_spider import MaisonsSpider


#TODO: 1-Scraping 2-Scoring

def Scraping():
    '''Appeler le Scraping'''
    process = CrawlerProcess()
    
    process = process.crawl(MaisonsSpider)
    
def Scoring():
    '''Construire le Scoring'''
    maisons = pd.read_csv(maisons_path)
    
    to_csv(flip_net_return)
            

if __name__ == "__main__":
    Scraping()
    
    Scoring()
    