import bs4
import requests
"""A webscrapping program to display the group table details of the FIFA WORLD CUP 2018"""


res = requests.get("https://www.fifa.com/worldcup/groups")


def group(id):
    bs_obj = bs4.BeautifulSoup(res.text, "html.parser")
    bs_obj1 = bs_obj.find_all('table', attrs={'id': id})
    table = bs_obj1[0].select("tbody")
    team = table[0].select("tr")
    for i in range(len(team)):
        if i == 4:
            break
        name = team[i].select(".fi-table__teamname")
        match_played = team[i].select(".fi-table__matchplayed")
        win = team[i].select(".fi-table__win")
        draw = team[i].select(".fi-table__draw")
        pts = team[i].select(".fi-table__pts")
        val = name[0].getText().replace("\n", "")
        print("Team Name : " + val[:-3])
        print("Matches Played: " + match_played[0].getText())
        print("Wins: " + win[0].getText())
        print("Draw: " + draw[0].getText())
        print("Lose: " + str(int(match_played[0].getText()) - int(win[0].getText()) - int(draw[0].getText())))
        print("Points " + pts[0].getText())
        print("\n\n")


group_id = ["275075", "275077", "275079", "275081", "275083", "275085", "275087", "275089"]
group_name = ["A", "B", "C", "D", "E", "F", "G", "H"]

for i in range(8):
    print("----- Group "+group_name[i]+" -----")
    group(group_id[i])