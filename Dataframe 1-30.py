# This is a sample Python script.



#21. Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
import pandas as pd
import numpy as np

data =pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(data)

#2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam=pd.DataFrame(exam_data,index=labels)
print(exam)

#3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
print(exam.describe())
print(exam.info())

print(exam[0:3])

#5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
print(exam[["name","score"]])

#6. Write a Pandas program to select the specified columns and rows from a given data frame.
#Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.

print(exam.iloc[[1,3,5,6],[1,3]])

#7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
print(exam[exam["attempts"]>2])

#8. Write a Pandas program to count the number of rows and columns of a DataFrame.
count_rows=len(exam.axes[0])
count_col=len(exam.axes[1])
print("Rows count:" + str(count_rows))
print("Columns count:" + str(count_col))

#9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
print(exam[exam["score"].isnull()])

#10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
print(exam[exam["score"].between(15,20)])

#11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
print(exam[(exam["attempts"]<2) & (exam["score"]>15)])

#12. Write a Pandas program to change the score in row 'd' to 11.5.
exam.loc['d','score']=11.5
print(exam)

#13. Write a Pandas program to calculate the sum of the examination attempts by the students.
print("The sum of examination attempts is:")
print(exam["attempts"].sum())

#14. Write a Pandas program to calculate the mean score for each different student in DataFrame.
print(exam["score"].mean())

#15. Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.
exam.loc['k'] = ['Ana', 16.8, 2,'No']
print(exam)

exam=exam.drop('k')
print(exam)

#16. Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order
xam.sort_values(by=["name","score"],ascending=[False,True])
print(exam)

#17. Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False

exam['qualify']=exam['qualify'].map({'yes':True,'no':False})
print(exam)


#18. Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.
exam['name']=exam['name'].replace('James','Suresh')
print(exam)

#19. Write a Pandas program to delete the 'attempts' column from the DataFrame.
exam['name']=exam.pop('attempts')
print(exam)

#20. Write a Pandas program to insert a new column in existing DataFrame.
color=['red','blue','green','black','yellow','grey','white','blue','grey','black']

exam["color"]=color
print(exam)



#21. Write a Pandas program to iterate over rows in a DataFrame.
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
exam1=pd.DataFrame(exam_data)
print(exam1)

for index,row in exam1.iterrows():
    print(row['name'],row['score'])

#22. Write a Pandas program to get list from DataFrame column headers.
print(list(exam.columns.values))

#23. Write a Pandas program to rename columns of a given DataFrame
exam.rename(columns={'name':'names'},inplace=True)
print(exam)

#24. Write a Pandas program to select rows from a given DataFrame based on values in some columns.
print(exam.loc[(exam["score"]==12.5) & (exam["color"]=='red')])

#25. Write a Pandas program to change the order of a DataFrame columns.
exam=exam[['names','color','score','qualify']]
print(exam)

#26. Write a Pandas program to add one row in an existing DataFrame.
new = {'names':2,'color':'blue','score': 20.7,'qualify':'True'}
exam=exam.append(new, ignore_index=True)
print(exam)

#27. Write a Pandas program to write a DataFrame to CSV file using tab separator.

exam.to_csv('new_exam-file.csv', sep='\t', index=False)
new_exam = pd.read_csv('new_exam-file.csv')
print(new_exam)

#28. Write a Pandas program to count city wise number of people from a given of data set (city, name of the person).
city_data =pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily','Anne'],
             'city': ['California','Georgia','Los Angeles','California','Georgia','Georgia']})
labels = ['a', 'b', 'c', 'd', 'e', 'f']
print(city_data)

cityy = city_data.groupby(["city"]).size().reset_index(name='Count of people')
print(cityy)

#29. Write a Pandas program to delete DataFrame row(s) based on given column value.
exam = exam[exam.color != 'red']
print(exam)

#30. Write a Pandas program to widen output display to see more columns.
print(exam.head())
pd.set_option('display.max_rows', 500)
print(city_data)




