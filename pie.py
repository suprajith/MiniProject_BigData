import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


def pie():
	# Connect  to Database
	db = MySQLdb.connect(host="localhost",
	                   	 user="root",
	                     passwd="Asupra*007$",
	                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql="SELECT `Accident_Index`,`Casualty_Class`,`Sex_of_Casualty`,`Casualty_Severity`,`Casualty_Type` FROM `Casuality`"
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames
	df=pd.DataFrame([[j for j in i] for i in rows])

	# grouping the data frame by gender by taking counts of number of accidents 
	sex=df.groupby(df[2])[2].count()
	Casuality=df.groupby(df[3])[3].count()


	labels = 'Male', 'Female'
	sizes = [sex[1],sex[2]]
	explode = (0.01, 0.01) 
	# representation of gender by accidents using pie chart
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	ax1.set_title('ratio of male & female accidents')
	plt.show()
	# representation of severity of accidents using pie chart
	labels1 = 'Fatal', 'Serious','slight'
	sizes1 = [Casuality[1],Casuality[2],Casuality[3]]
	explode1 = (0.01, 0.01,0.01) 

	fig2, ax2 = plt.subplots()
	ax2.pie(sizes1, explode=explode1, labels=labels1,autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	ax2.set_title('ratio of accident severity')
	plt.show()
