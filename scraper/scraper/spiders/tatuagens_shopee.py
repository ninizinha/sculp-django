import scrapy
import json

class TatuagensShopeeSpider(scrapy.Spider):
    name = "tatuagens_shopee"
    allowed_domains = ["shopee.com.br"]
    start_urls = [  'https://shopee.com.br/api/v4/search/search_items?by=relevancy&keyword=tatuagem%20tempor%C3%A1ria&limit=20&newest=0&order=desc&page_type=search']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'resultados.json',
    }
    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('items', []):
            yield {
                'nome': item['item_basic']['name'],
                'preco': item['item_basic']['price'] / 100000,
                'url': f"https://shopee.com.br/{item['item_basic']['name'].replace(' ', '-')}-i.{item['item_basic']['shopid']}.{item['item_basic']['itemid']}"
            }
