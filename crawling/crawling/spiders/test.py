import scrapy
from items import SpeechItem


class vie_publique_discours(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.vie-publique.fr/discours/274275-conseil-des-ministres-du-7-mai-2020-consequences-epidemie-covid',
    ]

    def parse(self, response):
        discours = SpeechItem()
        discours.title = response.css('.h1::text').get().strip()
        discours.date = response.css('time::attr(datetime)').get()
        discours.text = response.css('.field--name-field-texte-integral p').get()
        print(discours)
