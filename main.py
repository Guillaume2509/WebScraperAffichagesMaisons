from scrapy.crawler import CrawlerProcess
from CueilletteInformations.CueilletteInformations.spiders.cueillette_spider import MaisonsSpider


if __name__ == "__main__":
    process = CrawlerProcess()

    process.crawl(MaisonsSpider)