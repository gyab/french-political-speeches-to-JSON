# french-political-speeches-to-json

Scrape all speeches of the French governement uploaded on https://www.vie-publique.fr/discours.

- To scrape the website, [Scrapy](https://github.com/scrapy/scrapy) is used.
- The URL of latest generated JSON file is https://raw.githubusercontent.com/gyab/french-political-speeches-to-json/master/speeches.json.

Example of structured data of a scraped speech:
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


## Install french-political-speeches-to-json

`git clone git@github.com:gyab/french-political-speeches-to-json.git`

## Use it

`scrapy runspider crawling/crawling/spiders/speeches.py -o speeches.json`

## Task list

- [ ] Send a request by mail when a speech is not fully accessible (text missing for example)
- [ ] Generate a RSS feed for each new feed
- [ ] Not generate each new JSON file from scratch, append each time instead
