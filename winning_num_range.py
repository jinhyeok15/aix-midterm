import csv
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


def calc_range(num):
    return int(num/10)*10 if num>=10 else 1


data = {
    1: 0,
    10: 0,
    20: 0,
    30: 0,
    40: 0
}


with open('src/lottery.csv') as file:
    csvreader = csv.reader(file)
    first = True
    for row in csvreader:
        if first:
            first = False
            continue
        for i in row[2:]:
            data[calc_range(int(i))] += 1

label = data.keys()
index = np.arange(len(label))
values = data.values()
bar = plt.bar(index, values)
plt.xlabel("번호대")
plt.ylabel("당첨횟수")
plt.xticks(index, label, fontsize=15)
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', size = 12)
plt.show()
