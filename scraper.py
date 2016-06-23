import sys
reload(sys)
sys.setdefaultencoding('UTF8')
from splinter import Browser
import scraperwiki
from datetime import datetime

with Browser('phantomjs') as browser:
    ids = ['580587871570', '580587871572', '580587871576',  '580587871574', '580587871578', '580587871581', '580587871583',
           '580587871586', '580690543975', '580690543976', '580690543977', '580690543978', '580587871589', '580587871592',
           '580690543979', '580690543980', '580587871594', '580587871595', '580587871596', '580587871604', '580690543984',
           '580690543981', '580690543982', '580587871597', '580587871598', '580587871599', '580587871600', '580587871601',
           '580587871602', '580587871603', '580690543983', '580587871605', '580587871604', '580587871606', '580587871607',
           '580587871608', '580587871609', '580587871610', '580587871611', '580690543986', '580690543985', '580587871630',
           '580690543999', '580690544008', '580587871631', '580587871632', '580690544012', '580587871638', '580690544013',
           '580690543974', '580587871639', '580690544018', '580587871640', '580690544030', '580946326769', '580587871642',
           '580997996508', '580997996509', '580587871643', '580587871644', '580997996511', '580587871646', '580690544037',
           '580587871647', '580690544038', '580587871648', '580690544039', '580587871649', '580587871650', '580587871651',
           '580587871652', '580587871653']
    for id_number in ids:
        url = 'http://www.ebay.co.uk/itm/4x-Hairpin-Table-Legs-All-Sizes-Colours-UKs-Fastest-Selling-3yrs-Running-/281574593097?var={}&hash=item418f275249'.format(id_number)
        browser.visit(url)
        price = browser.find_by_id('prcIsum').text
        length = browser.find_by_xpath('//select[@id="msku-sel-1"]//option[@selected="selected"]').first.text
        design = browser.find_by_xpath('//select[@id="msku-sel-2"]//option[@selected="selected"]').first.text
        finish = browser.find_by_xpath('//select[@id="msku-sel-3"]//option[@selected="selected"]').first.text
        material_type = browser.find_by_xpath('//select[@id="msku-sel-4"]//option[@selected="selected"]').first.text
        print price, length, design, finish, material_type
        todays_date = str(datetime.now())
        scraperwiki.sqlite.save(unique_keys=['date'], data={"length": length.strip(), "design": design, "finish": finish, "material_type": material_type, "price": price, "date": 
