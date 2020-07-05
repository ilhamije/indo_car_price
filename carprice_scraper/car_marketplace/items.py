# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarMarketplaceItem(scrapy.Item):
    # define the fields for your item here like:
    year = scrapy.Field()
    brand = scrapy.Field()
    model_name = scrapy.Field()
    price = scrapy.Field()
    odometer = scrapy.Field()
    transmission = scrapy.Field()
    fuel = scrapy.Field()
    location = scrapy.Field()
    
