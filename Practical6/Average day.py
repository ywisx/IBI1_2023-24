import matplotlib.pyplot as plt  
Activity=["Sleeping","Classes","Studying","TV","Music","Other"]
Time_spent=[8,6,3.5,2,1,3.5]

plt.figure()
plt.pie(Time_spent,labels=Activity,startangle=90)
plt.title("The average day of a university student")
plt.show()

plt.clf()