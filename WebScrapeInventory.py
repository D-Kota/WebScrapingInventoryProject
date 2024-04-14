# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup

# %%
def InventoryTest(s1):


#This function scrapes the inventory table for one specific rug collection. 

    
    url = s1
    r= requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    table = soup.find("table", class_="")
    
    headers = table.find_all("td")
    headers = headers[0:3]

    titles = []

    for i in headers:
        title = i.text
        titles.append(title)

    df= pd.DataFrame(columns=titles) 

    rows = table.find_all("tr")

    for i in rows[1:]:
        data = i.find_all("td")           
        row = [tr.text for tr in data]     
        l =len(df)                         
        df.loc[l]= row   

    return df.head(10)   



# %%
AdaliaTunceliCream = "https://www.karastanrugs.com/products/karastan-adalia-tunceli-cream"
AdaliaKahtaDarkGrey = "https://www.karastanrugs.com/products/karastan-adalia-kahta-dark-gray"
AdaliaAmaysaBlue =   "https://www.karastanrugs.com/products/karastan-adalia-amasya-blue"
AdaliaKumraCream = "https://www.karastanrugs.com/products/karastan-adalia-kumra-cream"
AdaliaKumraDarkGrey = "https://www.karastanrugs.com/products/karastan-adalia-kumra-dark-gray"
AdaliaIznikRust = "https://www.karastanrugs.com/products/karastan-adalia-iznik-rust"
AdaliaIznikCream = "https://www.karastanrugs.com/products/karastan-adalia-iznik-cream"
AdaliaIznikBrown = "https://www.karastanrugs.com/products/karastan-adalia-iznik-brown"

AdaliaListURL = [AdaliaTunceliCream,AdaliaKahtaDarkGrey,AdaliaAmaysaBlue,AdaliaKumraCream,AdaliaKumraDarkGrey,AdaliaIznikRust,AdaliaIznikCream,AdaliaIznikBrown]


# %%
InventoryTest(AdaliaKumraCream)



# %%
