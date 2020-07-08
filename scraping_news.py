# -*- coding: utf-8 -*-
"""
This program demonstrated harvesting/scraping textual data from web 
Created on Tue Jun  9 23:27:07 2020

@author: Thitthima
"""

from bs4 import BeautifulSoap
import requests

# Step 1: Create Request object - to get the webpage you want
request = requests.get("https://www.thestar.com.my/news/nation/2018/08/12/a-new-rock-for-batu-the-youngest-ever-mp-in-the-country-is-all-for-lowering-the-minimum-age-to-vote")

# Step 2: Get the page in text and store it locally
page = request.text

#Step 3: Parse page into soap object
soap = BeautifulSoap(page,'lxml')

#Step 4: Find the news heading using class object, get the text and display it
heading = soap.find('div', attrs={'class':'headline story-pg'})

head_text=heading.get_text().strip()

print(head_text)

print("Program ends")