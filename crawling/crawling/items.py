import scrapy


class SpeechItem(scrapy.Item):
    speech_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()
    topics = scrapy.Field()
    speakers = scrapy.Field()
