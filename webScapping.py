import requests
from bs4 import BeautifulSoup
import os

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def table():
    soup = get_soup(link)
    rows = soup.find_all("table")[0].find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        t = [ele.text.strip() for ele in columns]
        print(f"{t}")
        for i in range(0,len(t)):
            Y = str( t[i] )
            archivo2.write( Y +"\n")
        

def images():
    soup = get_soup(link)
    images = soup.find_all("img")
    t = [{"src": image.get("src"), "alt": image.get("alt")} for image in images]
    print(f"{t}")
    for i in range(0,len(t)):
        X = str( t[i] )
        archivo.write( X +"\n")
        

    
if __name__=="__main__":
    link=input("Copia y pega el link de la página a hacerle Web Scrapping: ")
    archivo=open("webscrapping_images.txt","w")
    images()
    archivo.close()
    archivo2=open("webScarpping_table.txt","w")
    table()
    archivo2.close()

#El link que se usó es https://es.wikipedia.org/wiki/Queen
