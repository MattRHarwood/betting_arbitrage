from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.oddschecker.com/football/english/premier-league', headers={'User-Agent': 'Mozilla/5.0'}).text

team_name = "Chelsea"

soup = BeautifulSoup(source, 'lxml')
soup_td = soup.find("td", title="Add " + team_name + " to betslip")
print(soup_td.prettify())
