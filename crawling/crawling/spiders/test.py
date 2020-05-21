import scrapy
from crawling.crawling.items import SpeechItem


class ViePubliqueDiscours(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.vie-publique.fr/discours/274275-conseil-des-ministres-du-7-mai-2020-consequences-epidemie-covid',
    ]

    def parse(self, response):
        discours = SpeechItem()
        discours['title'] = response.css('.h1::text').get().strip()
        discours['date'] = response.css('time::attr(datetime)').get()
        discours['text'] = \
            response.css('.field--name-field-texte-integral p').get()
        discours['tags'] = response.css("div.tagsBox a::text").getall()
        discours['topics'] = response.css("div.thematicBox a::text").getall()
        discours['speakers'] = \
            response.css("ul.line-intervenant a::text").getall()
        return discours
