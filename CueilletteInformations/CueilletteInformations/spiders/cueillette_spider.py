import scrapy

class MaisonsSpider(scrapy.Spider):
    name = "AffichageMaisons"
    
    start_urls = [
        "https://duproprio.com/fr/quebec-rive-sud/levis/maison-a-vendre/hab-5338-rue-saint-georges-744976#la-capitale"]
        
    def parse(self, response):
        page = response.url.split('/')[-1] #Juste obtenir la page, on peut parser comme on veut
        filename = "post-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)