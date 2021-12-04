import scrapy
from ..items import AmazonBooksItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1638614558&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response, **kwargs):

        items = AmazonBooksItem()
        all_books_list = response.css('.sg-col-inner')
        for books in all_books_list:
            product_name = books.css('.s-access-title::text').extract() #.a-color-base.a-text-normal
            product_author = books.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
            product_price = books.css('.a-spacing-top-small .a-price span').css('::text').extract()
            product_link = books.css('.s-image::attr(src)').extract()

            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_price'] = product_price
            items['product_link'] = product_link
            yield items
