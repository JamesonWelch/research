import csv
import os
from datetime import datetime

path = os.path.join(os.path.expanduser('~'), 'Projects', 'Python', 'Data_Mining', 'google_stock_data.csv.csv')
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header

data = []
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    # Parse datetime - .string parse datetime
    date = datetime.strptime(row[0], '%m/%d/%Y')
    # Convert 'Open', 'High', 'Low', and 'Close' to floats & 'Volume' to integer
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    # Append a list with these values to the data list
    data.append([date, open_price, high, low, close, volume, adj_close])

returns_path = os.path.join(os.path.expanduser('~'), 'Projects', 'Python', 'google_returns.csv')
file = open(returns_path, 'w')

writer = csv.writer(file)
writer.writerow(['Date', 'Return'])
for i in range(len(data) -1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])



    
    
