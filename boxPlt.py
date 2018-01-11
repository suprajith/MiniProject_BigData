import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def boxplt():
	# Connect to database
	db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="Asupra*007$",
                     db="Road_Safety")

	cursor = db.cursor()

	# Execute SQL select statement
	sql="SELECT `Accident_Index`,`Number_of_Vehicles`,`Number_of_Casualties`, `Accident_Severity`, `Urban_or_Rural_Area`,`Day_of_Week` FROM `Accident` " 
	
	cursor.execute(sql)
	rows=cursor.fetchall()

	#Transforming data into DataFrames
	df=pd.DataFrame([[j for j in i] for i in rows])
	data = df[1]
	#plotting  box plot for average number of vehicle involved per accident
	plt.boxplot(data,0, '',0)
	plt.title("Number Of Vehicles involved in per Accident")
	plt.xlabel("")
	plt.show()
	
	