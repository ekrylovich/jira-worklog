#! /usr/local/bin/python

from timesheet.XlsxParser import XlsxParser
from timesheet.TimesheetTracker import TimesheetTracker

# 		Setup
# ________________________________

year = 2022
month = 9
startDay = 1
endDay = 2
fileName = 'timesheet.xlsx'
host = {jiraHost}
pat = {PersonalAccessToken}

# ________________________________
# 		End setup

parser = XlsxParser(fileName)
worklogs = parser.parseXlsx(startDay=startDay, endDay=endDay+1, month=month, year=year)
totals = parser.total(worklogs)

print('Sum per ticket: ', totals)
print('Total sum: ', sum(totals.values()))

tracker = TimesheetTracker(host=host, pat=pat)
tracker.trackTime(worklogs)






