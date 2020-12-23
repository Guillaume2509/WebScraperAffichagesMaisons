from scrapy.crawler import CrawlerProcess
from CueilletteInformations.CueilletteInformations.spiders.cueillette_spider import MaisonsSpider


#TODO: 1-Scraping 2-Scoring
            

if __name__ == "__main__":
    process = CrawlerProcess()

process.crawl(MaisonsSpider)

    maisons = pd.read_csv(maisons_path)
    
    print(flip_net_return)
    