import re
import scrapy
from car_marketplace.items import CarMarketplaceItem


class CarmudiSpider(scrapy.Spider):
    name = 'carmudi'
    allowed_domains = ['carmudi.co.id']
    start_urls = [
        'http://www.carmudi.co.id/cars/used/xenia/', 
        'http://www.carmudi.co.id/cars/used/jazz/', 
        'http://www.carmudi.co.id/cars/used/ertiga/', 
        'http://www.carmudi.co.id/cars/used/swift/', 
        'http://www.carmudi.co.id/cars/used/serena/', 
        'http://www.carmudi.co.id/cars/used/livina/', 
        'http://www.carmudi.co.id/cars/used/sienta/', 
        'http://www.carmudi.co.id/cars/used/avanza/']

    def parse(self, response):
        res_url = response.url
        model_name = res_url.split('/')[-2]

        listing_mobil = response.xpath('//div[@class="catalog-listing-items-container"]//div[@class="catalog-listing-description-top"]')
        
        # print('LEN listing mobil: ', len(listing_mobil))
        for mobil in listing_mobil:
            item = CarMarketplaceItem()
            
            description = mobil.xpath('.//h3[@class="item-title type-m"]/a/text()').get()
            desc_list = description.split(' ')

            item['year'] = re.findall(r"\b\d{4}\b", description)[0]
            brand_index = desc_list.index(model_name.capitalize())
            item['brand'] = desc_list[brand_index-1]
            item['model_name'] = model_name

            price = mobil.xpath('.//div[@class="attributes-wrapper"]//a/text()').get()
            item['price'] = price

            attr_list = mobil.xpath('.//div[@class="attributes-wrapper"]/ul[@class="inline-list catalog-listing-attribute-list"]//span/text()').extract()

            item['odometer'] = attr_list[0]
            item['transmission'] = attr_list[1]
            item['fuel'] = attr_list[2]
            item['location'] = attr_list[3]
            

            yield item