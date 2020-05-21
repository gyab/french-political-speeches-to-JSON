import scrapy


class SpeechItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    topics = scrapy.Field()
    speakers = scrapy.Field()
