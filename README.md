HowTo:

1. Open timesheet.xlsx and put hours for each ticket and day in 'Creative' and 'Other' sheets.
2. Copy all tracked time to 'Total' sheet [point to improvement]
3. Open 'trackMyTime.py' and populate setup properties in 'Setup section': 
    - year - year for which you want to track time
    - month - month for which you want to track time
    - startDay - start day from which you want track time from timesheet.xlsx
    - endDay - end day (including) from which you want track time from 'timesheet.xlsx'
    - fileName - file name where data is stored (timesheet.xlsx)
    - host - your Jira URL
    - pat - you 'Personal Access Token' from Jira (https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)
4. Install required python dependencies. Use pip3 or pip according to your local setup: 
    - pip3 install pandas
    - pip3 install JIRA