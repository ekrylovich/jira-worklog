#! /usr/local/bin/python
from jira import JIRA


class TimesheetTracker:

    def __init__(self, host, pat):
        self.host = host
        self.pat = pat

    def trackTime(self, worklogs):
        jira = self.jira()
        for key in worklogs:
            ticket = key
            worklogItems = worklogs[key]
            for worklogItem in worklogItems:
                workdayDay = worklogItem['day']
                workdayTime = worklogItem['time']
                print(f'Ticket: {ticket}, Year: {workdayDay.year}, Month: {workdayDay.month}, Day: {workdayDay.day}, Time: {workdayTime}')
                jira.add_worklog(issue=ticket, timeSpent=f"{workdayTime}h", started=workdayDay)

    def jira(self):
        host = self.host
        pat = self.pat

        headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
        headers["Authorization"] = f"Bearer {pat}"
        jira = JIRA(server=host, options={"headers": headers})
        return jira
