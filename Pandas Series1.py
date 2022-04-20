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


