import matplotlib.pyplot as plt 

# Activities and corresponding average time spent per day  
Activities = {'Sleeping': 8,'Classes': 6,'Studying': 3.5,'TV': 2,'Music': 1,'other':3.5} 
labels = Activities.keys()  
sizes = Activities.values() 

#If we want to know the average time spent on "Sleeping"
activity_name = input("Enter the name of an activity: ") 
average_hours_per_activity = Activities[activity_name]  
print(f"The average number of hours spent on {activity_name} is: {average_hours_per_activity} hours")

#Setting up pie charts
plt.figure(figsize=(10, 7))   
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90) 
plt.axis('equal') 
plt.title('Average Daily Activities of a University Student') 

# Show Pie Chart 
plt.show()

#Close Pie Chart
plt.clf()


