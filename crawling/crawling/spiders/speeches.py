import scrapy
from crawling.items import SpeechItem


class ViePubliqueDiscours(scrapy.Spider):
    name = 'speeches'

    start_urls = ['https://www.vie-publique.fr/discours']

    def parse(self, response):
        speech_page_links = response.css('.teaserSimple--title a')
        yield from response.follow_all(speech_page_links, self.parse_speech)

        pagination_links = response.css('li.pager__item a')
        print(pagination_links)
        yield from response.follow_all(pagination_links, self.parse)

    def parse_speech(self, response):
        discours = SpeechItem()
        discours['title'] = response.css('h1::text').get().strip()
        discours['date'] = response.css('time::attr(datetime)').get()
        discours['text'] = response \
            .css('.field--name-field-texte-integral p') \
            .get()
        discours['tags'] = response.css("div.tagsBox a::text").getall()
        discours['topics'] = response.css("div.thematicBox a::text").getall()
        discours['speakers'] = response \
            .css("ul.line-intervenant a::text").getall()
        return dict(discours)
