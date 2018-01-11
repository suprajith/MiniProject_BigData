# Main program importing all the modules

import sys
import urban_rural as pl
import multiline as ml
import pie as pi 
import stackbar as st 
import weather as we 
import multibar2 as ml2
import multiBarCharts as ml3
import boxPlt as bx
import prob_speedlimit as sl

# Calling other modules from the main program

def callfunction():
	while 1:
		print("welcome to road traffic injury survey: ")
		print("===============================")
		print("-------select the survey-------")
		print(" 1. URBAN or RURAL area ")
		print(" 2. Days_of_week by multiline graph ")
		print(" 3. Ratio of Gender_of_Driver and Accident Severity Using pie Charts")
		print(" 4. Age Band and Gender_of_Driver using Multibar plot ")
		print(" 5. Severity and Gender_of_Driver using Multibar Plot ")
		print(" 6. Light Conditions using Stacked graph ")
		print(" 7. Weather Conditions using Stacked graph ")
		print(" 8. Number of Vehicles involved per accident using Boxplot ")
		print(" 9. Speed Limit of Vehicles During Accident with Probability ")
		print(" 10. Exit")
		print("................................")
		choice=input("please enter the survey choice")
		if choice is 1:
			pl.urban_rural()
		elif choice is 2:
			ml.multiline()
		elif choice is 3:
			pi.pie()
		elif choice is 4:
			ml2.multibar()
		elif choice is 5:
			ml3.multibar3()
		elif choice is 6:
			st.light()
		elif choice is 7:
			we.weather()
		elif choice is 8:
			bx.boxplt()
		elif choice is 9:
			sl.hist()
		elif choice is 10:
			sys.exit()
			




# Main Function

if __name__ == '__main__':
	callfunction()