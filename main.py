from scrapy.crawler import CrawlerProcess
from CueilletteInformations.CueilletteInformations.spiders.cueillette_spider import MaisonsSpider


maisons_path = "path.csv"
            

if __name__ == "__main__":
    process = CrawlerProcess()

process.crawl(MaisonsSpider)

    maisons = pd.read_csv(maisons_path)
    