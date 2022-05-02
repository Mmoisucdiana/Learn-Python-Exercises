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

