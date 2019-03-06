import requests
from BeautifulSoup import BeautifulSoup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

symbol = ''

while symbol != 'stop':

	print "Which stock you want to analyze? Enter 'stop' to end."
	symbol = raw_input()

	if symbol == 'stop':
		quit()
		sys.exit()

	estimate = None
	current = None

	# STOCKTWITS NO LONGER ALLOWS WEB SCRAPING
	# API DOES NOT PROVIDE SENTIMENT DATA

	# url = 'https://stocktwits.com/symbol/' + symbol
	# response = requests.get(url)
	# html = response.content

	# soup = BeautifulSoup(html)

	# table = soup.find('ol', attrs={'class': 'stream-list show-conversation stream-poller'})
	    
	# fileWrite = open("stocktwits.txt","w")

	# for row in table.findAll('li'):
	# 	# print row.prettify();
	# 	fileWrite.write(row.prettify())

	# fileWrite.close()

	# # fileRead = open("stocktwits.txt","r")
	# # print fileRead.read()

	# data = open('stocktwits.txt').read()
	# totalBullish = data.count('bullish')
	# totalBearish = data.count('bearish')

	# fileWrite.close()

	url = 'https://finance.yahoo.com/quote/' + symbol 
	response = requests.get(url) 
	html = response.content

	soup = BeautifulSoup(html)
	estimate = soup.find('td', attrs={'class': 'Ta(end) Fw(600) Lh(14px)', 'data-test': 'ONE_YEAR_TARGET_PRICE-value'})

	if estimate != None:
		fileWrite = open("yFinanceEst.txt","w")
		fileWrite.write(estimate.prettify())		
		fileWrite.close()
		fileRead = open('yFinanceEst.txt')
		lines = fileRead.readlines()
		est = lines[2]
		fileRead.close()

	soup = BeautifulSoup(html)
	estimate = soup.find('span', attrs={'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})

	if estimate != None:
		fileWrite = open("yFinanceCurrent.txt","w")
		fileWrite.write(estimate.prettify())		
		fileWrite.close()
		fileRead = open('yFinanceCurrent.txt')
		lines = fileRead.readlines()
		current = lines[1]
		fileRead.close()

	if current == None or estimate == None:
		print('Error with scraping')
	else:
		exit = "graph"

		print 'Line graph (1) or bar graph (2)?'
		graphChoice = raw_input()

		if graphChoice == '1':
			fig = plt.figure()
			ax = fig.add_subplot(111)
			A = 0, 1
			B = current, est
			plt.plot(A,B)
			for xy in zip(A,B):
				ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
			plt.title('1y Increase')
			plt.grid()
			plt.show()

	# elif graphChoice == '2':
	# 	objects = ('Bullish', 'Bearish')
	# 	y_pos = np.arange(len(objects))
	# 	performance = [totalBullish, totalBearish]
		 
	# 	plt.bar(y_pos, performance, align='center', alpha=0.5)
	# 	plt.xticks(y_pos, objects)
	# 	plt.ylabel('Number of Related Comments')
	# 	plt.title('Expectations')
		 
	# 	plt.show()