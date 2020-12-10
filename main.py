from scrapy.crawler import CrawlerProcess
from CueilletteInformations.CueilletteInformations.spiders.cueillette_spider import MaisonsSpider

#TODO: créer le sous-projet et réajuster l'architecture du code: https://youtu.be/Wp6LRijW9wg
 #a
#spider

class MaisonsSpider(scrapy.Spider):
    name = "AffichageMaisons"
    
    start_urls = [ #à corriger, de cierto
        "https://duproprio.com/page/1"
        "https://remax.com"
        "https://royallepage.com"]
        
    def parse(self, response):
        page = response.url.split('/')[-1] #Juste obtenir la page, on peut parser comme on veut
        filename = "post-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            

if __name__ == "__main__":
    process = CrawlerProcess()

    process.crawl(MaisonsSpider)