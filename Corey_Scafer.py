import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')

"""
with open('comic.png' , 'wb') as f:
    f.write( r.content )
"""

#print( r.status_code )

#print( r.ok )

print( r.headers )

