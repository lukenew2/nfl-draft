import lxml as lxml
from bs4 import BeautifulSoup
from requests import get
import os
import pandas as pd

# The base url where the data we desire is located
BASE_URL = "https://www.fantasypros.com/nfl/adp/ppr-overall.php"
# Header which allows our webscraper to appear more human
headers = ({"user-agent":
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
# Test to see if webpage is responding correctly
r = get(BASE_URL)
print(r) # Should print out '<Response [200]>'

def make_adp_df():
    r = get(BASE_URL)
    page_html = BeautifulSoup(r.text, 'html.parser') # Extracts html from webpage
    table = page_html.find('table', id='data') # Finds the table from html
    df = pd.read_html(str(table))[0] # Extracts data from html table
    print("Output after reading html:\n\n", df.head(), '\n')
    df = df[["Player Team (Bye)", "POS", "AVG", "ESPN"]] # Filters important columns
    print("Output after filtering columns:\n\n", df.head(), '\n')
    df["PLAYER"] = df["Player Team (Bye)"].apply(lambda x: ' '.join(x.split()[:-2])) # Extract players name
    df["POS"] = df["POS"].str.extract(pat='([A-Z]+)') # Remove position rank

    df = df[["PLAYER", "POS", "AVG", "ESPN"]].sort_values("AVG") # Sort players by ADP

    print("Final output:\n\n", df.head(15))

    return df

df = make_adp_df()

PROJECT_ROOT_DIR = "."
FANTASY_FBALL_PATH = os.path.join(PROJECT_ROOT_DIR, "datasets")
os.makedirs(FANTASY_FBALL_PATH, exist_ok=True)

df.to_csv(FANTASY_FBALL_PATH + "/ADP.csv", index=False)

BASE_URL = "https://www.fantasypros.com/nfl/projections/{position}.php?week=draft"

def make_projection_df():

    final_df = pd.DataFrame() # Create final dataframe for concatenation

    for position in ["rb", "qb", "te", "wr"]:

        r = get(BASE_URL.format(position=position)) # format our url with each position

        page_html = BeautifulSoup(r.text, 'html.parser')
        table = page_html.find('table', id='data') # Gets table html
        df = pd.read_html(str(table))[0] # Creates datafrome from table
        # For every table not listing kickers the data is multi-leveled. So we drop a level
        if position != "k":
            df.columns = df.columns.droplevel(level=0)
        # Fix player name to not include team
        df["PLAYER"] = df["Player"].apply(lambda x: ' '.join(x.split()[:-1]))
        # My league is PPR so we add receptions to fantasy points
        if 'REC' in df.columns:
            df["FPTS"] = df["FPTS"] + df["REC"] # Add receptions if they're in there

        df["POS"] = position.upper() # add a position column

        df = df[["PLAYER", "POS", "FPTS"]]
        final_df = pd.concat([final_df, df])


    final_df = final_df.sort_values(by="FPTS", ascending=False) # sort df in descending order on FPTS column

    return final_df

df = make_projection_df()

df.to_csv(FANTASY_FBALL_PATH + "/FPTS_PROJ.csv", index=False)