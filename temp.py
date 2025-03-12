import pandas as pd
import re

# Read original data
df = pd.read_csv('phone.csv')

# Initialize extra collums
mplist = []
levellist = []

#
for usage_category in df[' Usage Range']:
    
    #Find the digits in usage_category (e.g., 0 1, 7 9, 11)
    match = re.findall(r'\d+', usage_category)
    
    
    if match: # Avoids errors and ensures len != 0
        # If is a range, take the average (midpoint) of the bounds of the range.
        if len(match) > 1: 
            midpoint = sum(int(num) for num in match) / len(match)
        # else add 1 to the range (e.g., 11+ becomes 12) 
        elif re.search(r'\+', usage_category):
            midpoint = float(match[0]) + 1
        else:
            midpoint = float(match[0])
        
        """ if 3 > midpoint >= 0:
            levellist.append('Low')
        elif 7 > midpoint >= 3:
            levellist.append('Medium')
        elif midpoint >= 7:
            levellist.append('High') """
        # Code above rewritten in one line
        # Build the ' Severity' collumn based on ranges (Low: 0-3; Medium: 3-7; High: 7+)
        levellist.append('Low' if 3 > midpoint >= 0 else 'Medium' if 7 > midpoint >= 3 else 'High' if midpoint >= 7 else 'N/A')


        mplist.append(midpoint)


df[' Midpoint'] = mplist
df[' Severity'] = levellist



## Calculate data for all students as well as within each usage severity category

# sum the results of multiplying the midpoint of each range with the number of people in the range
total_hours = sum(mp * ge for mp, ge in zip(df[' Midpoint'], df[' # of Students'])) # Total hours spent on phones by all students

total_ge = sum(a for a in df[' # of Students']) # Total students

total_average = round(total_hours/total_ge, 2) # Average screen time



# Totalled hours for each category
low_hours, med_hours, high_hours = (sum(mp * ge for mp, ge in zip(df[df[' Severity'] == level][' Midpoint'], df[df[' Severity'] == level][' # of Students'])) for level in ('Low', 'Medium', 'High'))

# Total # of students in each severity category
low_ge, med_ge, high_ge = (sum(df[df[' Severity'] == level][' # of Students']) for level in ('Low', 'Medium', 'High'))

# Average screen time in each category
low_average, med_average, high_average = round(low_hours/low_ge, 2), round(med_hours/med_ge, 2), round(high_hours/high_ge, 2)


## Determine the highest category
values = {'low': low_hours, 'medium': med_hours, 'high': high_hours}

highest_category = max(values, key=values.get)
highest_hours = values[highest_category]


## Print results
print("Data Table\n")

print(df, '\n')

print("Additional Data:\n")

print(f"The {highest_category} usage group had the highest screen time usage with {round(highest_hours/total_hours*100, 2)}% of classroom phone usage")


print(low_hours, '/', low_ge, '=', low_average)   

print(med_hours, '/', med_ge, '=', med_average)

print(high_hours, '/', high_ge, '=', high_average)   


