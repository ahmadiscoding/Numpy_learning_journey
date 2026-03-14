# Create an array of 365 Celsius temperatures. Convert to Fahrenheit using vectorized formula. Use np.where to label each day as 'Hot'(>30°C), 'Mild'(10-30), or 'Cold'(<10). Find hottest/coldest month by reshaping to (12, ~30).


import numpy as np


#to generate random values we can use:
# np.random.randint(-5, 50, 365)
# (min, max, total values)

celsius= np.random.randint(-5, 45, 365)

fahrenheit=  (celsius * 9/5)+32

# print(fahrenheit)

#used nested where() here bcz we can only give 3 arguments to each 
# where():
label= np.where((celsius<10), "Cold", np.where((celsius<=30), "mild", "hot"))
# print(label)


#This "celsius[:360]" just means take the first 360 values from the array.If your array has 365 days, we remove the last 5 days so the data fits perfectly into months.

#reshape is used to convert them in to 12 months and each with 30 days
#means 12 arrays with each containing 30 elements.

monthly_temp= celsius[:360].reshape(12,30)
# print(monthly_temp)


#FINDING AVERAGE OF EACH MONTH:
avg_monthly= monthly_temp.mean(axis= 1)
print(avg_monthly)

# FINDING HOTTEST TEMP OF EACH MONTH:

#here "+1" bcz the python index starts from 0 while the months start from 1
hot_month= np.argmax(avg_monthly) +1
print(hot_month)

#FINDING COLDEST TEMP OF EACH MONTH:

#here "+1" bcz the python index starts from 0 while the months start from 1
cold_month= np.argmin(avg_monthly)+1
print(cold_month)
