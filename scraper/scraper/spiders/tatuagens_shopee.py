import scrapy

class TatuagensShopeeSpider(scrapy.Spider):
    name = "tatuagens_shopee"
    allowed_domains = ["shopee.com.br"]
    start_urls = ["https://shopee.com.br/search?keyword=tatuagem%20temporaria"]

    def parse(self, response):
        for produto in response.css('div.shopee-search-item-result__item'):
             item =  {
                'nome': produto.css('div._10Wbs-::text').get(),
                'preco': produto.css('span._341bF0::text').get(),
                'link': response.urljoin(produto.css('a::attr(href)').get()),
                'imagem': produto.css('img::attr(src)').get(),
            }
             if item['nome'] and item['preco']:
                yield item
