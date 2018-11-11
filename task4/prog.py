import csv
import datetime
import matplotlib.pyplot as plt


def csv_reader(fo):
    reader = csv.reader(fo)
    arr = []
    for it in reader:
        it.append(getday(it[0]))
        arr.append(it)
    return arr

def getday(date):
    # 0 -  пн  6 - вс
    if date == 'Date': return 0
    year, month, day = (int(x) for x in date.split('-'))
    n = datetime.date(year, month, day)
    return n.weekday()

def count_day_sum(arr):   #Date,Open,High,Low,Close,Volume,Adj Close,day
    sum = [0] * 5
    for i in range(1,len(arr)):
        sum[arr[i][7]] += int(arr[i][5])
    return sum

def get_middle_year(arr):
    middle = [0] * 6
    count = [0] * 6
    for i in range(1, len(arr)):
        year, _, _, = (int(x) for x in arr[i][0].split('-'))
        middle[year-2012] += float(arr[i][6])
        count[year-2012] += 1
    for i in range(0,6):
        middle[i] = middle[i]/count[i]
    return middle

def print_middle_year(arr):
    for i in range(0,6):
        print(2012+i,'=',arr[i])
    return 0

def barplot(x_data, y_data, error_data, x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    # Draw bars, position them in the center of the tick mark on the x-axis
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')
    # Draw error bars to show standard deviation, set ls to 'none'
    # to remove line between points
    ax.errorbar(x_data, y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 2, capthick = 2)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

if __name__ == "__main__":
    csv_f = "apple.csv"
    arr = []
    with open(csv_f, "r") as fo:
        arr = csv_reader(fo)

    sum_of_day = count_day_sum(arr)

    #print(get_middle_year(arr))
    print_middle_year(get_middle_year(arr))

    barplot([1,2,3,4,5],[1,1,1,1,],0)
