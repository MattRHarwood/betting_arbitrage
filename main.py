import Scraping2.py as scrape
from datetime import datetime

def main():
    teams = ["x", "y", "z"]
    odds = [3]
    x = 1
    while(x):
        if (datetime.now().minute == (0 or 15 or 30 or 45)):
        for i in range(0, 3):
            scrape.odds(teams[i])
    if abitrage(odds):
        place_bet(odds, website)
    

if __name__ == "__main__":
    main()