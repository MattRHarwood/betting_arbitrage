from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def get_epl_match_urls() -> list:
    try:
        url = "https://www.oddschecker.com/football/english/premier-league"
        odds_checker_source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
        soup = BeautifulSoup(odds_checker_source, "lxml")
        match_links =[]
        for link in soup.find_all("td", class_="betting link-right"):
            match_links.append("https://oddschecker.com" + link.a['href'])
        return match_links
    except:
        print("error making active match url list")

#the class of the odd container varies in different matches, this might be why its throwing an error, inspect the html of the match
def get_match_csv(active_match_url: str) -> "csv":

    odds_table_source = requests.get(active_match_url, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(odds_table_source, "lxml")
    odd_rows = soup.find_all("tr", class_ = "diff-row evTabRow bc")
    teams = [row["data-bname"] for row in odd_rows]
    odds = []
    book = []
    team_list = []
    for i in range(0,len(odd_rows)):
        for entry in odd_rows[i].find_all("td", {"class": ["bc bs o", "bc bs oi", "bc bs b", "bc bs oo"]}):
            odds.append(entry["data-odig"])
            book.append(entry["data-bk"])
            team_list.append(teams[i])
    csv_file = open("change_me.csv", 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Dec_Odds', 'Book', 'Result'])
    for i in range(0, len(odds)):
        csv_writer.writerow([odds[i], book[i], team_list[i]])
    csv_file.close()
    

def get_match_df(active_match_url: str) -> pd.DataFrame:

    odds_table_source = requests.get(active_match_url, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(odds_table_source, "lxml")
    odd_rows = soup.find_all("tr", class_ = "diff-row evTabRow bc")
    teams = [row["data-bname"] for row in odd_rows]
    odds = []
    book = []
    team_list = []
    for i in range(0,len(odd_rows)):
        for entry in odd_rows[i].find_all("td", {"class": ["bc bs o", "bc bs oi", "bc bs b", "bc bs oo"]}):
            odds.append(entry["data-odig"])
            book.append(entry["data-bk"])
            team_list.append(teams[i])

    df = pd.DataFrame(list(zip(odds, book, team_list)), columns =['Dec_Odds', 'Book', 'Result'])
    return df

matches = get_epl_match_urls()

get_match_csv("https://www.oddschecker.com/ufc-mma/conor-mcgregor-v-dustin-poirier/winner")







