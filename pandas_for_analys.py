import pandas as pd

#asfreq - able to add new rows inn data if it is a date. You can set interval, that will cover
#shift - return previuous/future value in data seriees
s1 = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2022-01-01', '2022-01-03', '2022-01-06', '2022-01-08']))
s1 = s1.asfreq(freq = '1d', method = 'pad')
s1.fillna(s1.shift(1),inplace =True )
print(s1)


#Fillna can also take dict or series and so it is possible to change different columns in different ways simultaneously  
df = pd.DataFrame(data = {'user' : ['Ivan', 'Petr', 'Alex', 'Den'], 'user.speed' : [40, None, 42, 35], 'user.bag_weight' : [8, None, 2, 4]})
print(df.fillna({'user.speed':df['user.speed'].mean(), 'user.bag_weight': df['user.bag_weight'].median()}))
