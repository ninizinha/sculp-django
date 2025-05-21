# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(".")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_sculp.settings")
import django
django.setup()

from sculp.models import Tatuagem

class ScraperPipeline:
    def process_item(self, item, spider):
        Tatuagem.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item['preco'],
                'link': item['link'],
                'imagem': item['imagem']
            }
        )
        return item

