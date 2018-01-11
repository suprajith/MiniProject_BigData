import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def multiline():
	# Connect to database
	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Asupra*007$",
                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql="SELECT `Accident_Index`, `Accident_Severity`, `Urban_or_Rural_Area`,`Day_of_Week` FROM `Accident` "
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames
	objects=["2009","2010","2011","2012","2013","2014","2015"]
	count=np.arange(len(objects))
	df=pd.DataFrame([[j for j in i] for i in rows])
	values=[]
	# year wise frequency of accidents by on a day( 7 days of a week)
	for k in range(len(objects)):
		df1=df.loc[df[0].str.startswith(objects[k])]
		ypos=df1.groupby(df1[3])[3].count()
		print(ypos)
		values.append([ypos[1],ypos[2],ypos[3],ypos[4],ypos[5],ypos[6],ypos[7]])

	line=[]
	line2=[]
	for i in range(7):
		for j in range(7):
			line2.append(values[j][i])
		line.append(line2)
		line2=[]
	print(line)

	names=[2009,2010,2011,2012,2013,2014,2015]
	objects = np.arange(0,7,1)
	#multi line graph reprenting each day of week over 7 years
	plt.plot(objects,line[0],label='sunday')
	plt.plot(objects,line[1],label='monday')
	plt.plot(objects,line[2],label='tuesday')
	plt.plot(objects,line[3],label='wednesday')
	plt.plot(objects,line[4],label='thursday')
	plt.plot(objects,line[5],label='friday')
	plt.plot(objects,line[6],label='saturday')
	plt.xticks(count,names)
	plt.xlabel("years")
	plt.ylabel("frequency of Accidents")
	plt.legend()
	plt.show()



	# Close the connection
	db.close()