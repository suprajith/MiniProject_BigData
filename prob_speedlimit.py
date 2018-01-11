import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

def hist():
	# Connect
	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Asupra*007$",
                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	'''sql = "SELECT `Accident_Index`,`Accident_Severity`,`Number_of_Vehicles`,`Number_of_Casualties`,`Date`,`Day_of_Week`,`Time`,`Road_Type`,`Speed_limit`,`Carriageway_Hazards` FROM `Accident` " '''
	sql = "SELECT `Accident_Severity`,`Number_of_Vehicles`,`Number_of_Casualties`,`Date`,`Day_of_Week`,`Time`,`Speed_limit`,`Carriageway_Hazards` FROM `Accident` "
	
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames

	df=pd.DataFrame([[j for j in i] for i in rows])
	x = df[6]
	sns.distplot(x);
	plt.title("Probability Distribution")
	plt.xlabel("Speed Limit")
	plt.ylabel("Probability")
	plt.show()
#hist()
