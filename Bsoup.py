import urllib2
#from random import randrange
z=0
#yearurl=""
#monthurl=""
#dayurl=""
url1='http://www.express.co.uk/sitearchive/'

#http://www.express.co.uk/sitearchive/2016/12/1

for i in range(2009,2016):
	yearurl = url1+str(i)+"/"
	year=str(i)+"/"
	for j in range(01, 13):
		monthurl =yearurl+str(j)+"/"
		month=year+str(j)+"/"
		for k in range(1,31):
			dayurl=monthurl+str(k)
			day=month+str(k)
			print (dayurl)
			url=urllib2.urlopen(dayurl)
			page=url.read()
			from bs4 import BeautifulSoup
			f=open('test2.txt','a')
			for ul in BeautifulSoup(page).find_all('ul',{'class':'section-list'}):
				for span in ul.find_all('span'):
					out=span.text.encode('utf-8')
					#key=['killed','kills','killing','injuries','injury','injured','accident','safety','crash','protruding','mishaps','mishap','road','road-accident','death']
					key=['accident','Accident','accidents','Accidents']
					print(all(key) in str(out).lower().split())
					if any(x in str(out).lower().split() for x in key):
						f.write(out + "|" + day +'\n')
						z+=1
						print(z)
			f.close()



		





