"""
<p>You are given the following information, but you may prefer to do some research for yourself.</p>
<ul><li>1 Jan 1900 was a Monday.</li>
<li>Thirty days has September,<br />
April, June and November.<br />
All the rest have thirty-one,<br />
Saving February alone,<br />
Which has twenty-eight, rain or shine.<br />
And on leap years, twenty-nine.</li>
<li>A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.</li>
</ul><p>How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?</p>

"""

import euler_math as em

def solve(debug=False):
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def days_to_next_month(year, month, day=1):
        days = month_days[month]
        if month == 1 and (year % 400 == 0 or (year % 4 == 0 and year % 100 > 0)):
            days += 1
        
        return days
    
    year = 1901  # year
    month = 0  # month of year (0-indexed)
    day = 1  # first of month
    wday = 2  # Monday, day of week (0-indexed)
           
    sunday_count = 0
    while year < 2001:
        if wday == 0:
            if debug:
                print(f"{year}-{month+1}-{day} was a Sunday")
            sunday_count += 1
            
        mdays = days_to_next_month(year, month)
        wday = (wday + mdays) % 7
        month = (month+1) % 12
        year = year + (0 if month > 0 else 1)
    
    print(sunday_count)