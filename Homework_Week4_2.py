'''
==============================
Case Study 2 - Bird Migration
==============================
'''

#In this case study, we will continue taking a look at patterns of flight 
#for each of the three birds in our dataset.

#------------------------------------------------------------------------------

#Exercise 1
#----------

#pandas makes it easy to perform basic operations on groups within a dataframe 
#without needing to loop through each value in the dataframe. The sample code 
#shows you how to group the dataframe by birdname and then find the average 
#speed_2d for each bird. Modify the code to assign the mean altitudes of each 
#bird into an object called mean_altitudes.

#load the dataframe
import pandas as pd 

birddata = pd.read_csv('/Users/Admin/Desktop/bird_tracking.csv')

# First, use `groupby` to group up the data.
grouped_birds = birddata.groupby("bird_name")

# Now operations are performed on each group.
mean_speeds = grouped_birds.speed_2d.mean()

# The `head` method prints the first 5 lines of each bird.
print grouped_birds.head()

# Find the mean `altitude` for each bird.
# Assign this to `mean_altitudes`.
mean_altitudes = grouped_birds.altitude.mean()

#------------------------------------------------------------------------------

#Exercise 2
#----------

#In this exercise, we will group the flight times by date and calculate the 
#mean altitude within that day. Use groupby to group the data by date.

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# Check the head of the column.
print birddata.date.head()

grouped_bydates = birddata.groupby("date")

#Calculate the mean altitude per day and store these results as 
#mean_altitudes_perday.

mean_altitudes_perday = grouped_bydates.altitude.mean()

#------------------------------------------------------------------------------

#Exercise 3
#----------

#birddata already contains the date column. To find the average speed for each 
#bird and day, create a new grouped dataframe called grouped_birdday that 
#groups the data by both bird_name and date.

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()

# look at the head of `mean_altitudes_perday`.
mean_altitudes_perday.head()

#------------------------------------------------------------------------------

#Exercise 4
#----------

#Great! Now find the average speed for each bird and day. Store these are three 
#pandas Series objects – one for each bird.

#Use the plotting code provided to plot the average speeds for each bird.

import matplotlib.pyplot as plt

eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()

#------------------------------------------------------------------------------