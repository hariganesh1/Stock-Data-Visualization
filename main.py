import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# ERROR: File not found issues. 
# Deal with file I/O later
'''file_name = input(
    "Enter the filename of a yahoo finance .csv file with stock data.\n" 
    "This file must be downloaded on your computer."
) '''
file = "AAPL (1)_full.csv"
df = pd.read_csv(file)
open = df['Open']
close = df['Close']
vol = df['Volume']

NUMROWS = df.shape[0]

## Profit
profit = []
for i in range(0, NUMROWS):
    profit.append(abs(close[i] - open[i]))
print(f"The biggest absolute difference in the open price and the close price on the same day is ${round(max(profit),2)}")


## Visualization: 
fig = plt.figure()
# fig, axs = plt.subplots(2,2, sharey='row')



# Open plot
openPlot = fig.add_subplot(2,2,1)
openPlot.plot(open)
openPlot.set_title('Open Price Plot')

# Close plot
closePlot = fig.add_subplot(2,2,2)
closePlot.plot(close)
closePlot.set_title('Close Price Plot')
closePlot.set_ylabel('Dollars')


# Profit plot
profitPlot = fig.add_subplot(2,2,3)
profitPlot.plot(profit)
profitPlot.set_title('Profit Plot')
profitPlot.set_ylabel('Dollars')

# Volume plot
volumePlot = fig.add_subplot(2,2,4)
volumePlot.plot(vol)
volumePlot.set_title('Stock Volume Plot')
volumePlot.set_ylabel('Number of Shares (Millions)')

fig.supxlabel('Days since stock opened')

plt.show()





