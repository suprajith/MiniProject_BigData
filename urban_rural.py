import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


def urban_rural():
	# Connect to Database
	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Asupra*007$",
                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql="SELECT `Accident_Index`, `Accident_Severity`, `Urban_or_Rural_Area`,`Day_of_Week` FROM `Accident`"
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrame
	df=pd.DataFrame([[j for j in i] for i in rows])

	#User input request
	choice=input("1.urban  2.rural : select your choice")
	ypos=df[df[2] ==choice]

	# grouping the data frame by days of week by taking counts of urbun or rural from user input 
	ypos1=ypos.groupby(df[3])[3].count()
	print(ypos1)
	values= [ypos1[1],ypos1[2],ypos1[3],ypos1[4],ypos1[5],ypos1[6],ypos1[7]]
	objects=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
	count=np.arange(len(objects))


	#bar graph to show the urbun or rural area by frequency of accidents over days of week 
	plt.bar(count,values,align='center')
	plt.xticks(count,objects)
	plt.xlabel("days of week")
	plt.ylabel("frequency of Accidents")
	if choice == 1:
		plt.title("Urban")
	elif choice == 2:
		plt.title("Rural")
	plt.show()

	# Close the connection
	db.close()
