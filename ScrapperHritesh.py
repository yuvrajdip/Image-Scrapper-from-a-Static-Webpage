from bs4 import *
import requests as rq
import os 

r2 = rq.get("https://www.gettyimages.com/photos/virat-kohli-odi?family=editorial&phrase=virat%2520kohli%2520odi&sort=mostpopular")

soup2 = BeautifulSoup(r2.text,"html.parser")

links = []

x = soup2.select('img[src^="https://media.gettyimages.com/photos/"]')

for image in x :
    links.append(image['src'])

"""
for l in links:
    print( l )

"""

os.mkdir('kuli5')

i=290

for img_link in links:
    if i<= 550 :
        img_data = rq.get( img_link).content
        with open("kuli5\\" + str( i+1)+'.jpg', 'wb+') as f :
            f.write( img_data)
        i +=1 
    else:
        f.close()
        break
