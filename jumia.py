import re
import requests
from bs4 import BeautifulSoup


URL = "https://www.jumia.co.ke/"


def getstatuscode(URL):
    '''We want to see if we scrape the site'''
    response = requests.get(URL)
    return response.status_code


def getsoup(URL):
    if getstatuscode(URL) == 200:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print('Here is the status code: ', getstatuscode(URL))

def getproductname(soup):
    '''Get the name of a particular product'''
    name_lst = re.findall('<div>(.+)</div>', str(soup.find_all('h1', {'class':'name'})))

    if len(name_lst) > 0:
        productname = name_lst[0].capitalize()
        return productname
    else:
        print("No product name was scraped")
        return None
    
    def getprice(soup):
        '''Get the prie of the product'''
    price_lst = re.findall('KSH\$([0-9.,]+)', str(soup.find_all('span', {'class':'prc'})))

    if len(price_lst) > 0:
        price = float(price_lst[0])
        return price
    else:
        print("No price data was scraped")
        return None
    
    def getproduct(URL):
        '''Get all the essential product data'''
    try:
        soup = getsoup(URL)
        
        name = getname(soup)
        price = getprice(soup)

        return [name, price, URL]
    except:
        print('There was a problem scraping the product on this link: ', URL)
