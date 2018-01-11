import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

def multibar():
	# Connect to Database
	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Asupra*007$",
                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql = "SELECT `Sex_of_Driver`,`Age_Band_of_Driver` FROM `Vehicle` WHERE 1 "
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames
	df=pd.DataFrame([[j for j in i] for i in rows],columns = [0,1])
	print(df[1].unique())
	i=0
	lst = []
	# Converting real values of age into discrete values of age
	for x in df[1]:
		if x==-1:
			lst.append(-1)
		elif x <= 18:
			lst.append(0)
		elif (x > 40) & (x<61):
			lst.append(2)
		elif (x > 18) & (x<41):
			lst.append(1)
		else:
			lst.append(3)

	#Store the data in dataframe
	df[2] = np.array(lst)
	print(df.head())
	l = df.groupby([0,2]).count()
	freq = [x[0] for x in l.values]
	print(freq)

	N = 5
	men_means = freq[0:5]

	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, men_means, width, color='r')

	women_means = freq[5:10]

	rects2 = ax.bar(ind + width, women_means, width, color='y')

	# plotting multibar graph for Accidents by Age Group and Gender
	ax.set_ylabel('Number of Accidents')
	ax.set_xlabel('Age Band')
	
	ax.set_title('Accidents by Age Group and Gender')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels(('Unknown', 'Minor', 'Youth','Middle Aged','Old'))

	ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


	def autolabel(rects):

	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)

	plt.show()

