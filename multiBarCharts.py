import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

def multibar3():
	# Connect to Database
	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Asupra*007$",
                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql = "SELECT `Casualty_Class`, `Sex_of_Casualty`, `Age_Band_of_Casualty`, `Casualty_Severity`, `Casualty_Type`, `Casualty_Home_Area_Type` FROM `Casuality` "	
	
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames
	df=pd.DataFrame([[j for j in i] for i in rows],columns = [0,1,2,3,4,5])
	print(df.columns)
	l = df.groupby([1,3]).count()
	freq = [x[0] for x in l.values]
	print(freq)

	N = 3
	men_means = freq[0:3]

	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, men_means, width, color='r')

	women_means = freq[3:]

	rects2 = ax.bar(ind + width, women_means, width, color='y')

	# plotting graph for Accidents by Severity and gender
	ax.set_title('Accidents by Severity and gender')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels(('Fatal', 'Serious', 'Slight'))

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

