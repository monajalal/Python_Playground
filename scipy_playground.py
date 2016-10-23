import scipy
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pylab as plt
seas = seasonal_decompose(df['riders'])

fig = seas.plot()
fig.set_size_inches(12,8)
nums = [2, 3, 5]
print(scipy.mean(nums))

def stationarity(timeseries):

    #Determing rolling statistics
    rolling_mean = pd.rolling_mean(timeseries, window=12)
    rolling_std = pd.rolling_std(timeseries, window=12)

    #Plot rolling statistics:
    fig = plt.figure(figsize=(12, 8))
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolling_mean, color='red', label='Rolling Mean')
    std = plt.plot(rolling_std, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()

    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)


stationarity(df.riders)


'''
import fnmatch

print(fnmatch("Hello.txt", "*.txt"))
'''