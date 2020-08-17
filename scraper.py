import requests
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from product import Product
import utils
import web_driver_conf

amazon= "https://www.amazon.ca/"
amazon_pages = 5

if __name__ == "__main__":
    search = str(input("What are you looking for?\n:"))
    terms = search.split(" ")

    cheapest_price = 0.0
    best_discount = 0.0
    cheapest = Product("", "", "", "")
    best_deal = Product("", "", "", "")
    
    chrome_driver = web_driver_conf.get_chrome_web_driver()

    chrome_driver.get(amazon)
    element = chrome_driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    element.send_keys(terms)
    element.send_keys(Keys.ENTER)

    products = []

    for page in utils.my_range(amazon_pages, 0, 1, False):
        try:
            chrome_driver.get(chrome_driver.current_url + "&page=" + str(page))
        except:
            println('Error getting page ' + str(page))
            break

        for i in chrome_driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]'):
            counter = 0
            for element in i.find_elements_by_xpath('//div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a'):
                adding = True
                name = ""
                sale_price = ""
                normal_price = ""
                link = ""
                try:
                    name = i.find_element_by_tag_name('h2')[counter].text
                    sale_price = utils.convert_price_to_number(element.find_element_by_class_name('a-price').text)
                    link = i.find_elements_by_xpath('//h2/a')[counter].get_attribute('href')
                    try:
                        normal_price = utils.convert_price_to_number(element.find_element_by_class_name('a-text-price').text)
                    except:
                        Exception()
                        normal_price = sale_price
                except:
                    print("Exception")
                    adding = False

                product = Product(name, sale_price, normal_price, link)
                if (adding):
                    products.append(product)
                counter += 1
        print(page)

print(len(products))

for product in products:
    right = True
    for word in terms:
        if word.lower() not in product.name.lower():
            not_right = False

    if (right):
        if (product.price < lowest_price):
            cheapest_price = product.price
            cheapest = product

        discount = product.normal_price - product.sale_price
        if (discount < best_discount):
            best_discount = discount
            best_deal = product

with open('products.json', 'w') as json_file:
    data = {}
    data["Products"] = []
    for product in products:
        data["Products"].append(product.serialize())
    json.dump(data, json_file, sort_keys = True, indent = 4)

print(json.dumps(cheapest.serialize(), indent = 4, sort_keys = True))
print(json.dumps(best_deal.serialize(), indent = 4, sort_keys = True))
