import re
import requests
from bs4 import BeautifulSoup


URL = "https://www.jumia.co.ke/"


def getstatuscode(URL):
    '''We want to see if we scrape the site'''
    response = requests.get(URL)
    return response.status_code


def get_pagecontent(URL):
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
    
def getproductprice(soup):    
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
        

# calling out the functions and creating a
## list of list containing the data
soup = get_pagecontent(url)
name = getproductname(soup)
brand = getproductbrand(soup)
price = getproductprice(soup)
discount = getproductdiscount(soup)
review = getproductreviewcnt(soup)
rating = getproductrating(soup)

list_of_lists = [name, brand, price, discount, review,rating]

## Save and review the product data
with open('jumia_products.csv', 'w') as jumia_file:
    fieldnames = ["name", "brand", "price", "discount", "reviews", "rating"]
    
    csvwriter = csv.write(jumia_file)
    csvwriter.write(fieldnames)
    
    #loop through product list to update csv file
    for product in list_of_lists:
        csvwriter.write(product)
        
    print("Done! All products have been added to CSV file")

## Using pandas to do data manipulation
jumia = pd.read_csv('jumia_products.csv')
jumia.head(10)        
