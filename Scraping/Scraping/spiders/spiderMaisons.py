import scrapy
import re

class ScrapeListeAffichagesDuProprio(scrapy.Spider):
    
    #Nom du spider
    name = "scrapeListeAffichagesDuProprio"
    #URL de départ
    start_urls = ["https://duproprio.com/fr/rechercher/liste?search=true&cities%5B0%5D=633&type%5B0%5D=house&subtype%5B0%5D=1&subtype%5B1%5D=2&subtype%5B2%5D=4&subtype%5B3%5D=5&subtype%5B4%5D=6&subtype%5B5%5D=7&subtype%5B6%5D=9&subtype%5B7%5D=10&subtype%5B8%5D=11&subtype%5B9%5D=13&subtype%5B10%5D=15&subtype%5B11%5D=17&subtype%5B12%5D=19&subtype%5B13%5D=21&subtype%5B14%5D=97&subtype%5B15%5D=99&subtype%5B16%5D=100&is_for_sale=1&with_builders=1&parent=1&pageNumber=2&sort=-published_at"]
    #Fait intéressant, les listings de décuplent à partir de ce niveau dans css:
    #html.flexbox.flexwrap.flexboxlegacy.no-flexboxtweener.webp.webp-alpha.webp-animation.webp-losslessno-touch body.prov-qc.duproprio.notranslate main.container div.search-results-container div.search-results-listings-container div.search-results-listings-container__main-content div.search-results-listings ul.search-results-listings-list
    '''
    Multiples parse (en commentaire, pour plus tard)
    def parse(self, response):
        for post in response.css('html.flexbox.flexwrap.flexboxlegacy.no-flexboxtweener.webp.webp-alpha.webp-animation.webp-losslessno-touch body.prov-qc.duproprio.notranslate main.container div.search-results-container div.search-results-listings-container div.search-results-listings-container__main-content div.search-results-listings ul.search-results-listings-list')
            url = post.css('.ref') #Pas 100% sur avec le .ref, à voir
    '''
    #Le bon tutoriel: https://youtu.be/lNajD34Sfmg
    
    def parse(self, response):
        
        url = response.css('html.flexbox.flexwrap.flexboxlegacy.no-flexboxtweener.webp.webp-alpha.webp-animation.webp-losslessno-touch body.prov-qc.duproprio.notranslate main.container div.search-results-container div.search-results-listings-container div.search-results-listings-container__main-content div.search-results-listings ul.search-results-listings-list li#listing-941231.search-results-listings-list__item a.search-results-listings-list__item-image-link').extract()
        url = str(url)
        # url = url.replace(
        # TODO: Ajouter l'argument href à notre css pour bien recueillir l'url recherché.
        # Scraping recursively: https://stackoverflow.com/questions/34501458/crawling-a-site-recursively-using-scrapy
        

class ScrapeAffichagesIndividuelsDuProprio(scrapy.Spider):
    
    #Nom du spider
    name = "scrapeAffichagesIndividuelsDuProprio"
    
    #Liste des URL à Scraper
    start_urls = [
        "https://duproprio.com/fr/quebec-rive-sud/levis/maison-en-rangee-de-ville-a-vendre/hab-5897-rue-berlioz-920663"
        

    #Parser
    def parse(self, response):
        
        #Nom du fichier texte
        filename = 'maisons.csv'
        
        #Extraction de l'adresse, prix et surface
        try:
            adresse = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div/h1/text()').extract()
            adresse = str(adresse)
            adresse = adresse.replace('[\'', '').replace(',', '').replace('\']', '')
        except:
            adresse = "Failed to parse"

        try:
            prix = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/text()').extract()
            prix = str(prix)
            prix = prix.replace('\\xa0', '')
            prix = re.search("\\d+\\$", prix, re.MULTILINE).group()
        except:
            prix = "Failed to parse"

        try:
            surface = response.xpath('/html/body/main/div[1]/div/div[1]/section[1]/article/div[1]/div[4]/div[1]/div[2]/span[2]/text()').extract()
            surface = str(surface)
            surface = re.search("\\d*\\s?\\d*\\s?\\d+\\spi", surface, re.MULTILINE).group()
            surface = surface.replace(' ', '') + "2"
        except:
            surface = "Failed to parse"
        
        #Création d'une ligne type csv
        line = {"adresse":adresse, "prix":prix, "surface":surface}

        #Ajout de la ligne au fichier
        with open(filename, "w") as f:
        
            fieldnames = ['adresse', 'prix', 'prix']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    
            writer.writerrow(line)
    
