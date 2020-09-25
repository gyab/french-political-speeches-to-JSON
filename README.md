# french-government-statements-to-csv

Crawl and parse all the statements of the French government uploaded on https://www.vie-publique.fr/discours.

- To scrape the website, [Scrapy](https://github.com/scrapy/scrapy) is used.
- The URL of latest generated CSV file is https://raw.githubusercontent.com/gyab/french-government-statements-to-csv/master/statements.csv.

Structured data of a scraped statement:
  ```
  {
    "title": "Déclaration des chefs d'État et de gouvernement de Chypre, de l'Espagne, de la France, de la Grèce, de l'Italie, de Malte et du Portugal à l'issue du 7e Sommet des pays du sud de l'Union européenne, le 10 septembre 2020.",
    "date": "2020-09-10T12:00:00Z",
    "text": "1 - Nous, chefs d'État et de gouvernement de Chypre, de l'Espagne, de la France, de la Grèce, de..."
    "tags": [
      "International",
      "Relations internationales",
      "Politique étrangère"
    ],
    "topics": [
      "France - pays mediterraneens",
      "UE - Pays mediterraneens",
      "Sommet"
    ],
    "speakers": [
      "Présidence de la République"
    ]
  }
  ```

## Use it

The spider, used by [Scrapy](https://github.com/scrapy/scrapy) to crawl and parse the website, is located in `crawling/crawling/spiders`.

`scrapy runspider crawling/spiders/statements.py -o statements.csv`

## Task list

- [ ] Send a request by mail when a statement is not fully accessible (text missing for example)
- [ ] Generate a RSS feed for each new feed
- [ ] Not generate each new JSON file from scratch, append each time instead
- [ ] Publish the dataset as a Google Sheet
