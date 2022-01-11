import csv
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

weekends = {}
weekdays = {}

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    wr = open("newActivity.csv","w")
    wr.write(str(headerRow[0]) + "," + str(headerRow[1]) + ","+ str(headerRow[2]))
    wr.write("\n")

    n = 0 
    for row in reader :
        interval = int(row[2])
        if row[0] == "NA":
            row[0] = 0
            n += 1
        steps = row[0]
        times = pd.Timestamp(row[1])
        if times.dayofweek <5:
            row.append("weekdays")
            weekdays.setdefault(interval,[])
            weekdays[interval].append(int(steps))
        else:
            row.append("weekends")
            weekends.setdefault(interval,[])
            weekends[interval].append(int(steps))

        wr.write(str(row[0]))
        wr.write(str (row[0]) + "," + str (row[1]) + ","+ str (row[2]) + "," + str (row[3]))
        wr.write("\n")

    wr.close()

    weekends_list = []
    for i in weekends.keys():
        weekends_list.append(st.mean(weekends.get(i)))
    
    weekdays_list = []
    for i in weekends.keys():
        weekdays_list.append(st.mean(weekdays.get(i)))
        
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.title("5-minute intervals")
    plt.plot(weekends_list, c="blue")
    plt.plot(weekdays_list, c="red")
    plt.xlabel("5-minute Intervals")
    plt.ylabel("Average number of steps")
    plt.show()