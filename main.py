import scrapy

#TODO: sur la commande: scrapy startproject scrapyaffichagesmaisons

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
            
#TODO: sur la commande: scrapy crawl AffichageMaisons

'''TODO: sur la commande (plusieurs fonctions):
scrapy shell https://duproprio.com/ (s'assurer de mettre le bon argument, on a modifié par rapport au tutoriel)
response.css('title')'''
