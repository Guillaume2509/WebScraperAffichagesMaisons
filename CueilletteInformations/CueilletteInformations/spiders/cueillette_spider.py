import scrapy

class MaisonsSpider(scrapy.Spider):
    name = "AffichageMaisons"
    
    start_urls = [
        "https://duproprio.com/fr/quebec-rive-sud/levis/maison-a-vendre/hab-5338-rue-saint-georges-744976#la-capitale"]
        
    '''def parse(self, response):
        page = response.url
        filename = "essai_page_web1.html"
        with open(filename, "wb") as f:
            f.write(response.body)'''

    #parse2
    def parse(self, response):
        adresse = response.xpath('/html/body/main/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div/h1/text()').extract()
        filename = str(adresse) + '.txt'
        #filename = "essai_page_web1.txt"
        print(adresse)
        with open(filename, "w") as f:
            f.write(str(adresse))