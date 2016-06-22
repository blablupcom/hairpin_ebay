import sys
reload(sys)
sys.setdefaultencoding('UTF8')
import requests
from bs4 import BeautifulSoup as bs
import scraperwiki
from datetime import datetime


ua = {'User-agent': 'Mozilla/5.0'}
base_url = 'https://www.amazon.co.uk/Hairpin-Table-Legs-COMPLETE-Colours/dp/'


def connect(start_url):
    page = requests.get(start_url, headers=ua)
    return page

def parse(start_url):
    listing_soup = bs(connect(start_url).text, 'lxml')
    sizes_lis = listing_soup.find('div', id="variation_size_name").find('ul').find_all('li')
    for sizes_li in sizes_lis:
        sizes_url = base_url+sizes_li['data-defaultasin']
        listing_sizes_soup = bs(connect(sizes_url).text, 'lxml')
        colors_lis = listing_sizes_soup.find('div', id="variation_color_name").find('ul').find_all('li')
        size = sizes_li.find('span', 'a-size-base').text
        for colors_li in colors_lis:
            colors_ids = colors_li['id']
            if 'color_name_0' in colors_ids:
                color = 'Unfinished'
                price = listing_sizes_soup.find('span', id='priceblock_ourprice').text
                print price.encode('utf-8'), size, color
                todays_date = str(datetime.now())
                scraperwiki.sqlite.save(unique_keys=['Date'], data = {"Size": size.strip(), "Color": color.strip(), "Price": price.strip(), "Date": todays_date})
            if 'swatchUnavailable' in colors_li['class']:
                continue
            else:
                colors_url = colors_li['data-dp-url']
                if colors_url:
                    listing_color_soup = bs(connect('https://www.amazon.co.uk/Hairpin-Table-Legs-COMPLETE-Colours'+colors_url).text, 'lxml')
                    color = colors_li.find('img', 'imgSwatch')['alt']
                    price = listing_color_soup.find('span', id='priceblock_ourprice').text
                    print price.encode('utf-8'), size, color
                    todays_date = str(datetime.now())
                    scraperwiki.sqlite.save(unique_keys=['Date'], data = {"Size": size.strip(), "Color": color.strip(), "Price": price.strip(), "Date": todays_date})
                else:
                    continue


if __name__ == '__main__':
    parse('https://www.amazon.co.uk/Hairpin-Table-Legs-COMPLETE-Colours/dp/B00W1SELMM/ref=sr_1_1?ie=UTF8&qid=1466581141&sr=8-1&keywords=hairpin+legs')
