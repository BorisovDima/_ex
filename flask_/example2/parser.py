from lxml import html
import requests
from datetime import datetime
import re

class Parser:
    url = 'https://www.rbc.ru'
    text_filter_pattern = re.compile(r'')

    def parse_article(self, link):
        response = requests.get(link)
        page = html.fromstring(response.text)

        title = ' '.join(page.xpath('.//div[@class="article__header__title"]/span/text()'))
        image = ' '.join(page.xpath('.//div[@class="article__main-image"]//img/@src'))
        date = ' '.join(page.xpath('.//span[@class="article__header__date"]/@content'))
        subtitle = ' '.join(page.xpath('.//div[@class="article__text__overview"]/span/text()'))
        article = ''

        for el in page.xpath('.//div[contains(@class, "article__text")]//p | '
                             './/div[contains(@class, "article__text")]//ul '):
            try:
                self.filter_text(el)
                el_data = html.etree.tostring(el,  method='html', encoding='utf-8').decode('utf-8')
            except Exception as err:
                continue
            article += el_data
        return title, subtitle, article, self.format_date(date), image

    def filter_text(self, text):
        """
        Delete all links
        """
        for link in text.xpath('.//a'):
            link.tail = (link.text or '') + (link.tail or '')
        html.etree.strip_elements(text, 'a', with_tail=False)


    def format_date(self, string):
        try:
            return str(datetime.strptime(string.split('+')[0], '%Y-%m-%dT%H:%M:%S'))
        except Exception:
            return ''

    def __iter__(self):
        page = requests.get(self.url)
        text = html.fromstring(page.text)
        link = text.xpath('.//a[contains(@class, "main__big__link")]/@href')
        yield self.parse_article(link[0])
        for link in text.xpath('.//a[contains(@class, "main__feed__link")]/@href')[:9]:
            yield self.parse_article(link)


