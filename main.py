from scrapy.crawler import CrawlerProcess
from CueilletteInformations.CueilletteInformations.spiders.cueillette_spider import MaisonsSpider

#TODO: créer le sous-projet et réajuster l'architecture du code: https://youtu.be/Wp6LRijW9wg
            

if __name__ == "__main__":
    process = CrawlerProcess()

process.crawl(MaisonsSpider)