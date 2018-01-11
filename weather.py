import numpy as np
import matplotlib.pyplot as plt
import MySQLdb
import pandas as pd 

def weather():
	# Connect to Database
	db = MySQLdb.connect(host="localhost",
	                     user="root",
	                     passwd="Asupra*007$",
	                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql="SELECT `Accident_Index`,`Light_Conditions`,`Weather_Conditions` FROM `Accident`"
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames

	objects=["2009","2010","2011","2012","2013","2014","2015"]
	count=np.arange(len(objects))
	df=pd.DataFrame([[j for j in i] for i in rows])

	# grouping the data frame by Weather conditions and getting count of each weather condition.		
	values=[]
	for k in range(len(objects)):
		df1=df.loc[df[0].str.startswith(objects[k])]
		whether=df1.groupby(df1[2])[2].count()
		values.append([whether[1],whether[2],whether[3],whether[4],whether[5],whether[6],whether[7]])


	line=[]
	line2=[]
	for i in range(7):
		for j in range(7):
			line2.append(values[j][i])
		line.append(line2)
		line2=[]

	weather_1=line[0]
	weather_2=line[1]
	weather_3=line[2]
	weather_4=line[3]
	weather_5=line[4]
	weather_6=line[5]
	weather_7=line[6]



	# the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence
	names=[2009,2010,2011,2012,2013,2014,2015]



	#plotting stcked bar graph for diffrent weather conditions over years
	p1 = plt.bar(count, weather_1, width, color='green')
	p2 = plt.bar(count, weather_2, width, color='orange', bottom=weather_1)
	p3 = plt.bar(count, weather_3, width, color='yellow', bottom=weather_2)
	p4 = plt.bar(count, weather_4, width, color='grey', bottom=weather_3)
	p5 = plt.bar(count, weather_5, width, color='red', bottom=weather_4)
	p6 = plt.bar(count, weather_6, width, color='pink', bottom=weather_5)
	p7 = plt.bar(count, weather_7, width, color='blue', bottom=weather_6)


	plt.ylabel('frequency of Accident')
	plt.xlabel('years')
	plt.title('Weather conditions')
	plt.xticks(count,names)
	plt.legend((p1[0], p2[0],p3[0],p4[0],p5[0],p6[0],p7[0]), ('Fine no high winds', 'Raining no high winds',
		'Snowing no high winds','Fine + high winds','Raining + high winds','Snowing + high winds','Fog or mist'))

	plt.show()
