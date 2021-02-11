import requests
from bs4 import BeautifulSoup
import time

def CheckPrice():
    url = "https://www.hepsiburada.com/rampage-ad-rc4-siyah-2-125mm-2-70mm-isikli-fan-15-17-notebook-sogutucu-stand-p-HBV000007EXBY"
    headers = {"#PASTE HERE YOUR USER AGENT"}
    page = requests.get(url,headers = headers)
    info = BeautifulSoup(page.content,'html.parser')
    productName = info.find(id='product-name').get_text().strip()
    price = info.find(id='offering-price').get_text()
    main_price =int(price[1:5].replace(',',''))
    if(main_price <=130):
        print(f"{main_price} TL {productName} ON BİG SALE!")
    elif(main_price>130 and main_price<164):
        print(f"{main_price} TL {productName} ON SALE!")
        
    else:
        print(f"{main_price} TL {productName} NOT ON SALE")

while(True):
    CheckPrice()
    time.sleep(60*60)


    


