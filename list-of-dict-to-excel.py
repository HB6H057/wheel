# output a list of dictionaries to an excel sheet
import pandas as pd

players = [{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player1', 'bank': 0.06},
{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player2', 'bank': 4.0},
{'dailyWinners': 1, 'dailyFree': 2, 'user': 'Player3', 'bank': 3.1},
{'dailyWinners': 3, 'dailyFree': 2, 'user': 'Player4', 'bank': 0.32}]

df = pd.DataFrame.from_dict(players)

print (df)

df.to_excel('players.xlsx')
