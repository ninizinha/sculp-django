import scrapy

class TatuagensMLSpider(scrapy.Spider):
    name = "tatuagens_ml"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tatuagem-temporaria"]

    def parse(self, response):
        for produto in response.css('li.ui-search-layout__item'):
            yield {
                'nome': produto.css('h2.ui-search-item__title::text').get(),
                'preco': produto.css('span.price-tag-fraction::text').get(),
                'link': response.urljoin(produto.css('a::attr(href)').get()),
                'imagem': produto.css('img::attr(data-src)').get(),
            }

