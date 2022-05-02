# This is a sample Python script.


#PANDAS DATA SERIES
import pandas as pd
# 1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
import numpy as np

nr = pd.Series([12, 23, 34, 56])
print(nr)

# 2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
nr = pd.Series([12, 23, 34, 56])
print(nr)
print(type(nr))
print(nr.tolist())
print(type(nr.tolist()))

# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series. Go to the editor
# Sample Series: [2, 4, 6, 8, 10],[1, 3, 5, 7, 9]
even = pd.Series([2, 4, 6, 8, 10])
odd = pd.Series([1, 3, 5, 7, 9])
print(even)
print(odd)

ads = even + odd
print(ads)
sub = even - odd
print(sub)
multiple = even * odd
print(multiple)
divide = even / odd
print(divide)

# 4. Write a Pandas program to compare the elements of the two Pandas Series. Go to the editor
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
greater = even > odd
print(greater)
lower = even < odd
print(lower)
equal = even == odd
print(equal)

# 5. Write a Pandas program to convert a dictionary to a Pandas series.

dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(dict1)
sr = pd.Series(dict1)
print(type(sr))
print(sr)

# 6. Write a Pandas program to convert a NumPy array to a Pandas series. Go to the editor

nump = np.array([10, 20, 30, 40, 50])
print(type(nump))
nump_ser = pd.Series(nump)
print(nump_ser)
print(type(nump_ser))

# 7. Write a Pandas program to change the data type of given a column or a Series. Go to the editor
ser = pd.Series(['100', '200', 'python', '300.12', '400'])
print(ser)
integer = pd.to_numeric(ser, errors="coerce")
print(integer)

# 8. Write a Pandas program to convert the first column of a DataFrame as a Series. Go to the editor
import pandas as pd
import numpy as np

col = {"col1": [1, 2, 3, 4, 7, 11], "col2": [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=col)
print(df)
c1 = df.iloc[:, 0]
print(c1)
print(type(c1))

# 9. Write a Pandas program to convert a given Series to an array.
series = pd.Series(['100', '200', 'python', '300.12', '400'])
ar = np.array(series)
print(type(ar))
print(ar)

# 10. Write a Pandas program to convert Series of lists to one Series. Go to the editor
list = pd.Series([['Red', 'Green', 'White'],
                  ['Red', 'Black'],
                  ['Yellow']])

print(list)
l = list.apply(pd.Series).stack().reset_index(drop=True)
print(l)

# 11. Write a Pandas program to sort a given Series.
series = pd.Series(['100', '200', 'python', '300.12', '400'])
sorting = series.sort_values(ascending=True)
print(sorting)

# 12. Write a Pandas program to add some data to an existing Series
ser = pd.Series(['100', '200', 'python', '300.12', '400'])
# adding=ser.append(pd.Series(['500','PHP']))
# print(adding)

# 13. Write a Pandas program to create a subset of a given series based on value and condition.
set = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
v = 6
subset = print(set[set < v])

# 14. Write a Pandas program to change the order of index of a given series.
import pandas as pd

s = pd.Series(data=[1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
print(s)
s = s.reindex(index=['B', 'A', 'C', 'D', 'E'])

# 15. Write a Pandas program to create the mean and standard deviation of the data of a given Series.
nr = pd.Series([12, 23, 34, 56])
std_result = np.std(nr)
print("Standard deviation:", std_result)
mean_result = np.mean(nr)
print("Mean:", mean_result)

# 16. Write a Pandas program to get the items of a given series not present in another given series.
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([3, 4, 5, 6, 7])
missing = sr1[~sr1.isin(sr2)]
print(missing)
missing2 = sr2[~sr2.isin(sr1)]
print(missing2)

# 17. Write a Pandas program to get the items which are not common of two given series.
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([3, 4, 5, 6, 7])
union =pd.Series(np.union1d(sr1,sr2))
print(union)
intersection=pd.Series(np.intersect1d(sr1,sr2))
print(intersection)

#18. Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
nr = pd.Series([12, 23, 34, 56])
minim_result = np.min(nr)
print("Minimum:", minim_result)
maxim_result = np.max(nr)
print("Maximum:", maxim_result)
th=np.percentile(nr,[25,75])
print(th)

#19. Write a Pandas program to calculate the frequency counts of each unique value of a given series.
nr = pd.Series([12, 23, 34, 56,12,34,75,80,75,12,34,34,75,50,75])
unique_val=pd.Series(nr.unique())
print(unique_val)
repeating=pd.Series(nr.value_counts())
print(repeating)

#20. Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series.
nr = pd.Series([12, 23, 34, 56,12,34,75,80,75,12,34,34,75,50,75])
nr=pd.Series(nr.value_counts())
print(repeating)
result=nr[nr.isin(nr.value_counts().index[:1])]="other"
print(nr)


#21. Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
import pandas as pd

nr_series=pd.Series(np.random.randint(1,15,10))
print(nr_series)
multiple=np.where(nr_series % 5==0)
print(multiple)

#22. Write a Pandas program to extract items at given positions of a given series.
nr_series=pd.Series(np.random.randint(1,14,10))
print(nr_series)
pos=nr_series[0:4]
print(pos)
index=[1,2,3]
result = nr_series.take(index)
print(result)


#23. Write a Pandas program to get the positions of items of a given series in another given series.

series2=pd.Series([5,6,4,7,5,6])
#result=[pd.Index(series1).get_loc(s) for s in series2]
#print(result)

#24. Write a Pandas program convert the first and last character of each word to upper case in each word of a given series.
series=pd.Series(["python", "sql","matlab"])
upp=series.map(lambda x: x[0].upper()+x[1:-1]+ x[-1].upper())
print(upp)

series=pd.Series(["python", "sql","matlab"]) # just the first chr
upp1=series.map(lambda x: x[0].upper()+x[1:-1]+x[-1])
print(upp1)


#25. Write a Pandas program to calculate the number of characters in each word in a given series.
series=pd.Series(["python", "sql","matlab"])
chr1=series.str.len()
print(chr1)


#26. Write a Pandas program to compute difference of differences between consecutive numbers of a given series.
series3=pd.Series([2,6,7,8,10,12])
print(series3)

print(series3.diff().tolist())
print(series3.diff().diff().tolist())

#27. Write a Pandas program to convert a series of date strings to a timeseries.
time=pd.Series(["01 Jan 2015","10-02-2016","20180307","2014/05/06","2016-04-12"])
time1=pd.to_datetime(time)
print(time1)

#28. Write a Pandas program to get the day of month, day of year, week number and day of week from a given series of date strings.
from dateutil.parser import parse
date_series=pd.Series(["01 Jan 2015","10-02-2016","20180307","2014/05/06","2016-04-12"])
date_series = time.map(lambda x: parse(x))
print(date_series)
print(date_series.dt.day.tolist())
print(date_series.dt.dayofyear.tolist())
#print(date_series.dt.weekday_name.tolist())

#29. Write a Pandas program to convert year-month string to dates adding a specified day of the month.

date1 = pd.Series(['Jan 2019', 'Feb 2020', 'Mar 2021', 'Apr 2022'])
final_date = date1.map(lambda d: parse('15 ' + d))
print(final_date)

#31. Write a Pandas program to compute the Euclidean distance between two given series.
import numpy as np
series4=pd.Series([2,6,7,8,10,12])
series5=pd.Series([5,6,4,7,5,6])
dist=np.linalg.norm(series4-series5)
print(dist)


#32. Write a Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series.
import numpy as np
nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
print(result)


#33. Write a Pandas program to replace missing white spaces in a given string with the least frequent char.

str1 = 'abc def abcdef icd'
print("Original series:")
print(str1)
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)

#34. Write a Pandas program to compute the autocorrelations of a given numeric series.

number = pd.Series(np.arange(17) + np.random.normal(1, 14, 17))
print(number)
autocorr1 = [number.autocorr(i).round(2) for i in range(15)]
print(autocorr1[1:])

#35. Write a Pandas program to create a TimeSeries to display all the Sundays of given year.
timeseries=pd.Series(pd.date_range('2020-01-01',periods=52,freq="W-MON"))
print(timeseries)

#36. Write a Pandas program to convert given series into a dataframe with its index as another column on the dataframe.
char=list('ABCDRFSTFGG')
arrange=np.arange(9)
dict=dict(zip(char,arrange))
ser=pd.Series(dict)
datframe=ser.to_frame().reset_index()
print(datframe)


#37. Write a Pandas program to stack two given series vertically and horizontally.
nums1=pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1]) #horizontally
char1=pd.Series(['a','v','b','c','d','r','g','h','y','f'])
df=pd.concat([nums1,char1],axis=1)
print(df)

nums1=pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1]) # vertically
char1=pd.Series(['a','v','b','c','d','r','g','h','y','f'])
df=pd.concat([nums1,char1],axis=0)
print(df)

#38. Write a Pandas program to check the equality of two given series.
nums2=pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums3=pd.Series([1, 8, 7, 5, 6, 5, 5, 4, 8, 1])
eq=pd.Series.equals(nums2,nums3)
print(eq)
 #OR
nums2=pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums3=pd.Series([1, 8, 7, 5, 6, 5, 5, 4, 8, 1])
print(nums2==nums3)


#39. Write a Pandas program to find the index of the first occurrence of the smallest and largest value of a given series.
nums2=pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print(nums2.idxmax())
print(nums2.idxmin())

nums2=pd.Series([100, 200, 500, 200, 5, 3])
dict1 =pd.DataFrame({'Nan': [100], 'b': [200], 'c': [300], 'd': [500], 'e': [800]})

#40. Write a Pandas program to check inequality over the index axis of a given dataframe and a given series.

print(type(nums2))
print(type(dict1))
print(dict1.ne(nums2, axis = 0))
print(nums2)
print(dict1)






