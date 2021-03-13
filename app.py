import pandas as pd

schedule = pd.read_html("https://www.hockey-reference.com/leagues/NHL_2021_games.html")

df = schedule[0]

new_df = df[df["Home"] == "Buffalo Sabres"][["Date", "Visitor", "G", "Home", "G.1"]]

print(new_df)
