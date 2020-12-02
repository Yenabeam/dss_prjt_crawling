# -*- coding: utf-8 -*-


from selenium import webdriver
from fake_useragent import UserAgent
import pandas as pd
import time
import configparser
import pymongo
from datetime import datetime

def overview(keyword):
    

    url = 'https://m.joongna.com/search-list/product?searchword={}&dateFilter=1'.format(keyword)
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent={}".format(UserAgent().chrome))
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36")
    options.add_argument("headless")    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    tag = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div/button')

    links = driver.find_elements_by_css_selector('.pd_h20 div > div > a')
    print("loaded {} items!!!".format(len(links)))    
    df = []
    n=1

    for link in links:
        link = link.get_attribute('href')
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
#         options.add_argument("user-agent={}".format(UserAgent().chrome))
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36")

        driver = webdriver.Chrome(options=options)
        driver.get(link)
        time.sleep(1)
        try:
            title = driver.find_element_by_css_selector('.pd20 > p').text
            view_count = driver.find_element_by_css_selector('p .c_orange').text
            desc = driver.find_elements_by_css_selector('.ProductDetailComponent_tag__1sc7f.mb8')[0].text
            price = driver.find_element_by_css_selector('.pd20 strong').text
        except:
            print("err", end= " ")
            driver.quit()
            continue
        try:
            region = driver.find_elements_by_css_selector('button .f15')[0].text
        except:
            region = None           

        df.append({'title' : title, 'price' : price, 'region' : region, 'view_count' : view_count, 'desc' : desc, 'link' : link, 'market' : '중고나라', 'keyword' : keyword})
        driver.quit()
        print(n, end= " ")
        n+=1
        
    driver.quit()
    
    today = datetime.now()
    
    config = configparser.ConfigParser()
    config.read('/home/ubuntu/masterpiece/mongo.ini')
    mongodb_ip = config["mongo"]

    client = pymongo.MongoClient(mongodb_ip["ip_address"])
    db = client.joongo
    collection = db["C{}".format(today.strftime('%y%m%d%H'))]
    collection.insert(df)
    
    print("Done Crawling and Insert into Mongodb")
    
    return pd.DataFrame(df)