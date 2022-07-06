# Script to get the players data

from playwright.sync_api import sync_playwright

years = list(range(1991, 2023))

player_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for year in years:
        url = player_stats_url.format(year)
        page.goto(url)
        html = page.content()
        with open("player/{}.html".format(year), "w+") as f:
            f.write(html)
    browser.close()