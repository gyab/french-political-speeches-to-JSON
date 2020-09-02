from crawling.crawling.items import SpeechItem
from crawling.crawling.spiders.test import ViePubliqueDiscours

discours = SpeechItem()
spider = ViePubliqueDiscours()

discours = spider.parse()
