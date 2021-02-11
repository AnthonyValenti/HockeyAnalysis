# Basic usage of matplotlib to plot 3 differnt graphs comparing advanced stats of different NHL Players over the past
# 3 seasons

import pandas as pd
from matplotlib import pyplot as plt

print("Enter your Choice\n1: Individual Corsi VS Goals Scored\n2: Individual Corsi VS Fenwick\n3: Scoring Chances/60 vs "
      "Points\n--------------------")
choice = int(input("Option: "))

skaters = pd.read_csv('SkaterDataTeam.csv')
skaters1 = pd.read_csv('SkaterDataSolo.csv')
if choice == 1:
    corsi = []
    goals = []
    names = []
    for x in range(len(skaters1)):
        if (skaters1['TOI'][x] / skaters1['GP'][x]) >= 15:
            corsi.append(skaters1['iCF'][x])
            goals.append(skaters1['Goals'][x])
            names.append(skaters1['Player'][x])

    plt.scatter(goals, corsi)
    plt.title("Individual Corsi VS Goals Scored")
    plt.xlabel("Goals Scored")
    plt.ylabel("Corsi")
    for i, txt in enumerate(names):
        plt.annotate(txt, (goals[i], corsi[i]))

    plt.show()
if choice == 2:
    corsi = []
    fenwick = []
    names = []
    for x in range(len(skaters1)):
        if (skaters1['TOI'][x] / skaters1['GP'][x]) >= 15:
            corsi.append(skaters1['iCF'][x])
            fenwick.append(skaters1['iFF'][x])
            names.append(skaters1['Player'][x])

    plt.scatter(fenwick, corsi)
    plt.title("Individual Corsi VS Fenwick")
    plt.xlabel("fenwick")
    plt.ylabel("Corsi")
    for i, txt in enumerate(names):
        plt.annotate(txt, (fenwick[i], corsi[i]))

    plt.show()
if choice == 3:
    points = []
    chancesPer60 = []
    names = []
    for x in range(len(skaters1)):
        if 13 >= (skaters1['TOI'][x] / skaters1['GP'][x]) >= 5:
            points.append(skaters1['Total Points'][x])
            chancesPer60.append((skaters1['iSCF'][x]/skaters1['TOI'][x])*60)
            names.append(skaters1['Player'][x])

    plt.scatter(chancesPer60, points)
    plt.title("Points VS Scoring Chances")
    plt.xlabel("Scoring Chances per 60")
    plt.ylabel("Points")
    for i, txt in enumerate(names):
        plt.annotate(txt, (chancesPer60[i], points[i]))

    plt.show()
