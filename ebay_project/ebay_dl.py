import argparse
from telnetlib import STATUS
import requests
from bs4 import BeautifulSoup
import json
import csv

# take string and return number of items sold 

def parse_items_sold(s):
    accumulator = ''
    for char in s:
        if char in '1234567890':
            accumulator += char
    if 'sold' in s:
        return int(accumulator)
    else:
        return 0  
def parse_item_price(s):
    accumulator = ''
    if '$' in s:
        for char in s:
            if char in '1234567890':
                accumulator += char
            if char == ' ': 
                break 
        return int(accumulator)

def parse_shipping_price(s):
    accumulator = ''
    if 'free' in s.lower():
        return 0
    if '$' in s:
        for char in s:
            if char in '1234567890':
                accumulator += char
            if char == ' ':
                break
        return int(accumulator)
    else:
        return 0




parser = argparse.ArgumentParser(prog = 'Ebay Scraper',description = 'donwload info from ebay and store on JSON',)
parser.add_argument('search_term')
parser.add_argument('--num_pages', default=10)
parser.add_argument('--csv', default = False )
args = parser.parse_args()

print('args.search_terms =', args.search_term)

# have to download the first ten pages

items =[]

for page_number in range(1,int(args.num_pages)+ 1):
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+args.search_term+'&_sacat=0&LH_TitleDesc=0&_pgn='+ str(page_number)
    print('url -', url)

# download html
    r = requests.get(url)
    status = r.status_code

    print('status =', status )
    html = r.text
 
#  Process html

    soup = BeautifulSoup(html, 'html.parser')
    
    # loop over the tags for each item 
    tags_items =soup.select('.s-item')
    for tag_item in tags_items:

        # extract name
        item_names = tag_item.select(".s-item__title")
        for name in item_names:
            name = name.text

        #extract free returns 
        freereturns = False
        free_returns = tag_item.select(".s-item__free-returns")
        for free in free_returns:
            freereturns = True

        # extract number sold 
        items_sold = None 
        tags_items_sold = tag_item.select('.s-item__hotness')
        for tag in tags_items_sold:
            items_sold = parse_items_sold(tag.text)

        # Extract price
        tags_item_price = tag_item.select(".s-item__price")
        for tag in tags_item_price:
            price = parse_item_price(tag.text)

        #Extract shipping price in cents (requires function)
        tags_shipping = tag_item.select(".s-item__shipping , .s-item__freeXDays")
        shipping = None
        for tag in tags_shipping:
            shipping = parse_shipping_price(tag.text)
            
            

        # Extract status 
        tag_item_status = tag_item.select('.SECONDARY_INFO')
        for tag in tag_item_status:
            item_status = tag.text

        
        item= {'name':name , 'price': price , 'shipping' : shipping, 'free_returns' : freereturns,'items_sold': items_sold , 'item_status' : item_status }
        items.append(item)

print ('items=',items)


if args.csv:
    csv_filename = args.search_term+ '.csv'
    file = open(csv_filename, 'w',  encoding= 'utf-8')
    with file:

        header = items[0].keys()
        writer = csv.DictWriter(file, fieldnames= header)
        writer.writeheader()
        for item in items:
            writer.writerow(item)
else:
    filename = args.search_term+'.json'
    with open(filename, 'w' , encoding = 'utf-8') as f:
        f.write(json.dumps(items))











