import requests
import bs4

"""A webscrapping program to extract the headlines from the TOI website"""


res = requests.get("https://timesofindia.indiatimes.com/home/headlines")

try:
    res.raise_for_status()
    bs_obj = bs4.BeautifulSoup(res.text, "html.parser")
    content = bs_obj.findAll("div", attrs={"class": "headlines-list"})
    link = content[0].findAll("a")
    print("------NEWS FLASH------\n\n")
    print("TODAY'S HEADLINES\n")
    i = 0
    for news in link:
        if i == 0:
            pass
        else:
            print(str(i)+". "+news.get("title"))
            print("")
        i += 1
except:
    print("Sorry could not connect.Please try again later.")
