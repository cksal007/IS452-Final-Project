import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('/Users/Tiffanykim/PycharmProjects/IS452/Final Project/players.xlsx')
df.columns = df.iloc[0] #I defined the column names as the first row.
df.drop(0, inplace=True) # I dropped the first row because I don't need it anymore.
df = df[["FULL NAME", "TEAM", "POS", "AGE", "3P%", 'PPGPointsPoints per game.', 'RPGReboundsRebounds per game.', 'APGAssistsAssists per game.', 'SPGStealsSteals per game.', 'BPGBlocksBlocks per game.']]
df.columns = ["FULL NAME", "TEAM", "POS", "AGE", "3P%", 'PPG', 'RPG', 'APG', 'SPG', 'BPG']


# filter out by position
G = []
F = []
C = []
for row in df.values:
    row = list(row)
    if "G" in row[2]:
        G.append(row)
    elif "F" in row[2]:
        F.append(row)
    else:
        C.append(row)
# highest scoring guard in NBA
max_ppg1, max_ppg2 = -1, -1
max_player1, max_player2 = "", ""
for guard in G:
    ppg = guard[5]
    name = guard[0]
    if ppg > max_ppg1 and ppg > max_ppg2:
        if max_ppg1 == min([max_ppg1, max_ppg2]):
            max_player1 = name
            max_ppg1 = ppg
        else:
            max_player2 = name
            max_ppg2 = ppg
    elif ppg > max_ppg1 and ppg <= max_ppg2:
        max_player1 = name
        max_ppg1 = ppg
    elif ppg <= max_ppg1 and ppg > max_ppg2:
        max_player2 = name
        max_ppg2 = ppg

ppg_guards = [max_player1, max_player2]

# highest scoring forward in NBA
max_ppg1, max_ppg2 = -1, -1
max_player1, max_player2 = "", ""
for forward in F:
    ppg = forward[5]
    name = forward[0]
    if ppg > max_ppg1 and ppg > max_ppg2:
        if max_ppg1 == min([max_ppg1, max_ppg2]):
            max_player1 = name
            max_ppg1 = ppg
        else:
            max_player2 = name
            max_ppg2 = ppg
    elif ppg > max_ppg1 and ppg <= max_ppg2:
        max_player1 = name
        max_ppg1 = ppg
    elif ppg <= max_ppg1 and ppg > max_ppg2:
        max_player2 = name
        max_ppg2 = ppg

ppg_forwards = [max_player1, max_player2]

# highest scoring center in NBA
max_ppg = -1
max_player = ""
for center in C:
    ppg = center[5]
    name = center[0]
    if ppg > max_ppg:
        max_ppg = ppg
        max_player = name

ppg_center = max_player
ppg_team = ppg_guards + ppg_forwards + [ppg_center]

# youngest guards in NBA
min_age1, min_age2 = 100, 100
min_player1, min_player2 = "", ""
for guard in G:
    age = guard[3]
    name = guard[0]
    if age < min_age1 and age < min_age2:
        if min_age1 == min([min_age1, min_age2]):
            min_player1 = name
            min_age1 = age
        else:
            min_player2 = name
            min_age2 = ppg
    elif age <= min_age1 and age > min_age2:
        min_player1 = name
        min_age1 = age
    elif age > min_age1 and age <= min_age2:
        min_player2 = name
        min_age2 = age

young_guards = [min_player1, min_player2]

# youngest forwards in NBA
min_age1, min_age2 = 100, 100
min_player1, min_player2 = "", ""
for forward in F:
    age = forward[3]
    name = forward[0]
    if age < min_age1 and age < min_age2:
        if min_age1 == min([min_age1, min_age2]):
            min_player1 = name
            min_age1 = age
        else:
            min_player2 = name
            min_age2 = ppg
    elif age <= min_age1 and age > min_age2:
        min_player1 = name
        min_age1 = age
    elif age > min_age1 and age <= min_age2:
        min_player2 = name
        min_age2 = age

young_forwards = [min_player1, min_player2]

# youngest center in NBA
min_age = 100
min_player = ""
for center in C:
    age = center[3]
    name = center[0]
    if age < min_age:
        min_age = age
        min_player = name

young_center = min_player
young_team = young_guards + young_forwards + [young_center]

# oldest guards in NBA
max_age1, max_age2 = -1, -1
max_player1, max_player2 = "", ""
for guard in G:
    age = guard[3]
    name = guard[0]
    if age > max_age1 and age > max_age2:
        if max_age1 == min([max_age1, max_age2]):
            max_player1 = name
            max_age1 = age
        else:
            max_player2 = name
            max_age2 = age
    elif age > max_age1 and age <= max_age2:
        max_player1 = name
        max_age1 = age
    elif age <= max_age1 and age > max_age2:
        max_player2 = name
        max_age2 = age

old_guards = [max_player1, max_player2]

# oldest forwards in NBA
max_age1, max_age2 = -1, -1
max_player1, max_player2 = "", ""
for forward in F:
    age = forward[3]
    name = forward[0]
    if age > max_age1 and age > max_age2:
        if max_age1 == min([max_age1, max_age2]):
            max_player1 = name
            max_age1 = age
        else:
            max_player2 = name
            max_age2 = age
    elif age > max_age1 and age <= max_age2:
        max_player1 = name
        max_age1 = age
    elif age <= max_age1 and age > max_age2:
        max_player2 = name
        max_age2 = age

old_forwards = [max_player1, max_player2]

# oldest center in NBA
max_age = -1
max_player = ""
for center in C:
    age = center[3]
    name = center[0]
    if age > max_age:
        max_age = age
        max_player = name

old_center = max_player
old_team = old_guards + old_forwards + [old_center]

ppg_dict = {}
for player in df.values:
    ppg_dict[player[0]] = player[5]

age_dict = {}
for player in df.values:
    age_dict[player[0]] = player[3]

index = np.arange(5)
bar_width = 0.35

fig, ax = plt.subplots()
old = ax.bar(index, [ppg_dict[i] for i in old_team], bar_width, label="Old")
young = ax.bar(index + bar_width, [ppg_dict[i] for i in young_team], bar_width, label="Young")

ax.set_xlabel('PLAYER')
ax.set_ylabel('PPG')
ax.set_title('Oldest vs. Youngest team')

for rect in old:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

for rect in young:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
ax.legend()

plt.savefig("example.png")

valid = False
while not valid:
    response = input("Which team do you want to see?\n1. Youngest, 2. Oldest, 3. Highest PPG\n")
    if response == "1":
        valid = True
        print(young_team)
    elif response == "2":
        valid = True
        print(old_team)
    elif response == "3":
        valid = True
        print(ppg_team)
    else:
        print("invalid response: try again")

