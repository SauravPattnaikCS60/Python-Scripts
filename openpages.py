import bs4
import webbrowser
import requests

"""A simple program to to open three best links of anything searched in Google"""

link = input()
res = requests.get("https://www.google.co.in/search?q="+link)  # leave the format for now

try:
    res.raise_for_status()

    soupobj = bs4.BeautifulSoup(res.text, "html.parser")
    text = soupobj.select('.r a')
    size = min(3, len(text))
    for loc in range(size):
        webbrowser.open("www.google.com"+text[loc].get('href'))
except Exception as err:
    print(err)




