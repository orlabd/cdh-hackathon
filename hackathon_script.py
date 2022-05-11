import ox
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_pdf_id(keyword):
    api = ox.API('https://archive.leftove.rs/api/')
    tag_keyword = keyword

    item = api.findDocuments(
    {"keys":["id"],
     "query":{"conditions":[{"key":"*","value":keyword,"operator":"="}],"operator":"&"}})

    json_length = len(item["data"]["items"])
    id_list = []

    for i in range(json_length):
        id_list.append(item["data"]["items"][i]["id"])

    random_id = random.choice(id_list)

    return random_id

def scrape_url(pdf_id):
    url = "https://archive.leftove.rs/documents/" + str(pdf_id)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    time.sleep(5) 
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    file_name = soup.find('iframe')["src"]

    return file_name