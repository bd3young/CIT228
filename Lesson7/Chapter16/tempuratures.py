import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Lesson7\Chapter16\data\SanFranTemps.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    # get high temps
    dates, highs, lows = [], [], []
    for row in reader:
        currentDate = datetime.strptime(row[2], '%m/%d/%Y')
        high = int(row[3])
        low = int(row[4])
        dates.append(currentDate)
        highs.append(high)
        lows.append(low)

    # plot high temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c= 'red', alpha = 0.5)
    ax.plot(dates, lows, c = 'blue', alpha = 0.5)
    ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

    # format chart
    ax.set_title('Daily high and low Temps, for 2018 in San Francisco', fontsize = 18)
    ax.set_xlabel('Days', fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temps (F)', fontsize = 16)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()
