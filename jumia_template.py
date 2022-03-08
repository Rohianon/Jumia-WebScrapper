'''
If working on a local machine, consider doing a pip install <packagename> before proceeding with the scrapper.

Authored By:

        @rohianon48@gmail.com

        @2021
```
# Neccessary Imports
import 
import 
import 
import 
from  import 

url = 'Input URL you are scrapping here.'

# check for the response and whether the site can be scrapped.


# Product page Scrapper
def get_pagecontent(url):
    '''
    This helper function helps get the content from the site 
    and then gets to the required division so as to get the 
    required jumia products.
    parameter:
      url (str): a string of the cite you want to scrape
     returns:
      soup content(bs4 object):  from the required page
    '''
    # begin code here.
    
    return soup_content


## Retrieve product name
def getproductname(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product name
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_name (list) : list of product names
    '''
    #Extract product name from soup
    
    return product_name

## Retrieve Brand Name
def getproductbrand(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product brand
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_brand (list) : list of product brands
    '''
    # begin code here

    return product_brand

## Retrieve Price
def getproductprice(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    # begin code here
    
    return product_price

## Retrieve the Discount
def getproductdiscount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product discount
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_discount (list) : list of product discounts
    '''
    # begin code here
    
    return product_discount

## Retrieve the Number of reviews.
def getproductreviewcnt(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_reviews (list) : list of product reviews
    '''
    # begin code here
    

    return product_reviewcnt

## Retrieve the ratings.
def getproductrating(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    # begin code here
    

    return product_rating

## Retrieve the remaining stock.
def getproductcount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract remaining product stock
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_count (list) : list of product items remaining in stock
    '''
    # begin code here
    

    return product_count

# Bonus Knowledge.

## Determine the actual customer satisfaction rating.
## this function will be computed using pandas
def getactualrating(reviews, rating):
    '''
    Helper function uses the review and rating columns obtained from the created dataframe
    and then calculate the final actual rating.
    parameter:
      soup (bs4Object) : a beutiful soup object containing parsed html
    returns:
      product_price (list) : list of product prices
    '''
    # begin code here
    
    return actual_rating

# calling out the functions and creating a
## list of list containing the data
soup = get_pagecontent(url)
name = getproductname(soup)
brand = getproductbrand(soup)
price = getproductprice(soup)
discount = getproductdiscount(soup)
review = getproductreviewcnt(soup)
rating = getproductrating(soup)

list_of_lists = [____, ____, ____, ____, ____,____]

## Save and review the product data
with _____('jumia_products.csv', 'w') as jumia_file:
    fieldnames = ["name", "brand", "price", "discount", "reviews", "rating"]
    
    csvwriter = csv.____(jumia_file)
    csvwriter._____(fieldnames)
    
    #loop through product list to update csv file
    for ____ in _____:
        csvwriter._____(product)
        
    print("Done! All products have been added to CSV file")

## Using pandas to do data manipulation
jumia = pd.read_csv('jumia_products.csv')
jumia.head(10)
