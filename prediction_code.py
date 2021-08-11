import matplotlib.pyplot as plt
import pandas as pd
import statistics
plt.style.use('seaborn-whitegrid') 
df=pd.read_csv('NSE-TATAGLOBAL11.csv') 
x = df['Open'] 
y = df['Close'] 
plt.figure(figsize=(16,8)) plt.title('Open vs Close Price History') plt.plot(x, y, 'o')
plt.xlabel('Open Price INR(₹)', fontsize=14) plt.ylabel('Close Price INR(₹)')

#The model

# finding slope

meanx = mean(x) 
meany = mean(y) 
print(meanx,meany) meanxx = mean(x*x) 
meanxy = mean(x*y) 
m = ((meanx * meany) - meanxy) / ((meanx * meanx) - meanxx) 
print('The slope is:'+str(m)+'.')

# finding intercept 

b = meany - (m * meanx) 
print('The intercept is:' +str(b)) 

#Prediction using input

predicx = 3000 
predicy = ((m*predicx) + b)
print('The prediction of closing prices for opening price of 2800 : ' +str(predicy))