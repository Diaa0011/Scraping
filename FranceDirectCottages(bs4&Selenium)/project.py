from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# Create a driver object for Chrome browser
driver = webdriver.Chrome()

# Load the website
url = "https://www.brittany-ferries.co.uk/holidays/search?vt=0&s=ASC&p=8"

driver.get(url)
# Get the HTML content
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
# Find all the div elements with the class name "product"
content = soup.find_all("dd-product-card")
result = []
for prop in content:
    name = prop.find('h2').text
    propType = prop.find('h3').text
    link = prop.find(class_='item-content')
    if link.has_attr('href'):
        a_link = f"https://www.brittany-ferries.co.uk{link['href']}"
    else:
        a_link = "No Link"
    place = prop.find('p').text
    # rate = prop.find_all(class_='img')
    # a_rate = ""
    # for i in rate:
    #     if len(rate)<=3:
    #         a_rate = "normal"
    #     elif len(rate) == 4:
    #         a_rate = "high"
    #     else:
    #         a_rate = "premium"
    prop_info={
        'name':name,
        'property_Type':propType,
        'place':place,
        'link':a_link
    }
    print(prop_info)
    result.append(prop_info)
    time.sleep(2)

df = pd.DataFrame(result)
df.to_csv('Cottages_France.csv',index=False)

