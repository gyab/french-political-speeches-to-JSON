import scrapy


class ViePubliqueDiscours(scrapy.Spider):
    name = 'speeches'

    start_urls = ['https://www.vie-publique.fr/discours']

    def parse(self, response):
        speech_page_links = response.css('.teaserSimple--title a')
        yield from response.follow_all(speech_page_links, self.parse_speech)

        '''pagination_links = response.css('li.pager__item a')
        yield from response.follow_all(pagination_links, self.parse)'''

    def parse_speech(self, response):
        yield {
            'title': response.css('h1::text').get().strip(),
            'date': response.css('time::attr(datetime)').get(),
            'text': response.css('.field--name-field-texte-integral p').get(),
            'tags': response.css("div.tagsBox a::text").getall(),
            'topics': [x.strip() for x in response.css("div.thematicBox a::text").getall()],
            'speakers': response.css("ul.line-intervenant a::text").getall()
        }
