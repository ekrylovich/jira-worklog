#! /usr/local/bin/python
from datetime import datetime
import pandas


class XlsxParser:

	def __init__(self, file):
		self.file = file

	def isNaN(self, num):
		return num != num

	def parseXlsx(self, startDay, endDay, month, year):
		excel_data_df = pandas.read_excel(self.file, sheet_name='Total')
		worklogs = {}
		for index, row in excel_data_df.iterrows():
			worklogs[row['Jira ticket']] = []
			for day in range(startDay, endDay):
				if not self.isNaN(row[day]):
					dateTime = datetime(year, month, day, 8, 0, 0, 0)
					worklogs[row['Jira ticket']].append({
						"day": dateTime,
						"time": row[day]
					})
		return worklogs

	def total(self, worklogs):
		totalTime = 0
		sumPerTicket = {}
		for key in worklogs:
			worklogItems = worklogs[key]
			summa = 0
			for worklogItem in worklogItems:
				summa = summa + worklogItem['time']
			totalTime = totalTime + summa
			sumPerTicket[key] = summa
		return sumPerTicket
