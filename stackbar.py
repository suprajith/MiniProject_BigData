import numpy as np
import matplotlib.pyplot as plt
import MySQLdb
import pandas as pd 

def light():
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

	# grouping the data frame by light conditions and getting count of each light condition. 
	values=[]
	for k in range(len(objects)):
		df1=df.loc[df[0].str.startswith(objects[k])]
		light=df1.groupby(df1[1])[1].count()
		values.append([light[1],light[4],light[5],light[6],light[7]])


	line=[]
	line2=[]
	for i in range(5):
		for j in range(7):
			line2.append(values[j][i])
		line.append(line2)
		line2=[]

	light_1=line[0]
	light_4=line[1]
	light_5=line[2]
	light_6=line[3]
	light_7=line[4]


	# the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence
	names=[2009,2010,2011,2012,2013,2014,2015]


	#plotting stcked bar graph for diffrent light conditions over years
	p1 = plt.bar(count, light_1, width, color='blue')
	p2 = plt.bar(count, light_4, width, color='green', bottom=light_1)
	p3 = plt.bar(count, light_5, width, color='yellow', bottom=light_4)
	p4 = plt.bar(count, light_6, width, color='red', bottom=light_5)
	p5 = plt.bar(count, light_7, width, color='grey', bottom=light_6)


	plt.ylabel('frequency of Accident')
	plt.xlabel('years')
	plt.title('Light conditions')
	plt.xticks(count,names)
	plt.legend((p1[0], p2[0],p3[0],p4[0],p5[0]), ('Daylight', 'Darkness-lights lit','Darkness-lights unlit',
		        'Darkness-no lighting','Darkness-lighting unknown'))

	plt.show()

