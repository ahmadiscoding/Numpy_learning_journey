# Create a (4, 7) array = 4 weeks × 7 days of sales. Compute daily totals (axis=0), weekly totals (axis=1), find best/worst day per week, stack with previous month using vstack, compute month-over-month % change.


import numpy as np

# 4 weeks × 7 days sales
sales = np.array([
    [120,150,100,130,170,200,220],
    [140,160,120,150,180,210,230],
    [130,155,110,140,175,205,225],
    [150,170,130,160,190,220,240]
])

print("Sales Data:\n", sales)

# daily totals (column-wise)
daily_totals = sales.sum(axis=0)
print("\nDaily totals:", daily_totals)

# weekly totals
weekly_totals = sales.sum(axis=1)
print("\nWeekly totals:", weekly_totals)

# best day per week
best_day = sales.max(axis=1)
print("\nBest day each week:", best_day)

# worst day per week
worst_day = sales.min(axis=1)
print("\nWorst day each week:", worst_day)

# previous month data
previous_month = sales - 20

# stack months
combined = np.vstack((previous_month, sales))

print("\nCombined months:\n", combined)

# month over month % change
change = ((sales.sum() - previous_month.sum()) / previous_month.sum()) * 100

print("\nMonth-over-month % change:", round(change,2), "%")