# read csv in the folder

import pandas as pd
import numpy as np

# read csv in the folder
incident = pd.read_csv('INCIDENT.csv', sep=',', header=0)
shooter = pd.read_csv('SHOOTER.csv', sep=',', header=0)
victim = pd.read_csv('VICTIM.csv', sep=',', header=0)
cities = pd.read_csv('uscities.csv', sep=',', header=0)

# check the % of unique values for incident_id in the csvs and print it with the name of csv

# Uniqueness
print('incident_id in incident.csv: ',
      incident['Incident_ID'].nunique()/incident['Incident_ID'].count())
print('incident_id in shooter.csv: ',
      shooter['incidentid'].nunique()/shooter['incidentid'].count())
print('incident_id in victim.csv: ',
      victim['incidentid'].nunique()/victim['incidentid'].count())

# Conformity
# For each incident, check that the city column is inside in at least 1  "City" in the cities csv

# For each incident city
citiesArray = cities['city'].array
# calculate % of not fitting cities
notIn = 0
for city in incident['City']:
    # check if city is in the cities[city] column
    if city in citiesArray:
        continue
    else:
        notIn += 1

print('Not in cities: ', notIn/len(incident['City']))

# Completeness
# Print for every csv the percentage of missing values in each column
for column in incident.columns:
    print('Missing values in incident.csv column', column, ': ',
          incident[column].isnull().sum()/incident['Incident_ID'].count())
for column in shooter.columns:
    print('Missing values in shooter.csv column', column, ': ',
          shooter[column].isnull().sum()/shooter['incidentid'].count())
for column in victim.columns:
    print('Missing values in victim.csv column', column, ': ',
          victim[column].isnull().sum()/victim['incidentid'].count())

# Validity
# For incident check that dates are YY/MM/DD and print the percentage of not valid dates
# For shooter check that age is a number and print the pecentage of not valid ages
# For victim check that age is a number and print the percentage of not valid ages

# For each incident date
notValid = 0
for date in incident['Date']:
    #check that date has a format of YYYY/MM/DD
    try:
        pd.to_datetime(date, format='%Y/%m/%d')
    except ValueError:
        notValid += 1

print(f"Not valid dates %: {notValid/len(incident['Date'])}")

# For each shooter age
notValid = 0
for age in shooter['age']:
    #check that age is a number
    try:
        float(age)
    except ValueError:
        notValid += 1

print(f"Not valid ages for shooter: {notValid/len(shooter['age'])}")

# For each victim age
notValid = 0
for age in victim['age']:
    #check that age is a number
    try:
        float(age)
    except ValueError:
        notValid += 1

print(f"Not valid ages for victim: {notValid/len(victim['age'])}")
