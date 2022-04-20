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



#Collect and group data from different rows and columns together
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
table = pd.pivot_table(df, values='D', index=['A', 'B'],
                    columns=['C'], aggfunc=np.sum)
# RESULT
#    table
#   C        large  small
#    A   B
#    bar one    4.0    5.0
#        two    7.0    6.0
#    foo one    4.0    1.0
#        two    NaN    6.0
