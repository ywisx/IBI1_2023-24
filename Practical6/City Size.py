import numpy as np
import matplotlib.pyplot as plt

# Given data
UK_City=["Edinburgh","Glasgow","Stirling","London"]
China_City=["Haining","Hangzhou","Shanghai","Beijing"]
UK_Population=[0.56,0.62,0.04,9.7]
China_Population=[0.58,8.4,29.9,22.2]

#make dictionaries  
assert len(UK_City) == len(UK_Population), "城市和人口数量不匹配"   
UK_Data = {}   
for city, UK_Pop in zip(UK_City, UK_Population):  
    UK_Data[city] = UK_Pop  
print(UK_Data)

assert len(China_City) == len(China_Population), "城市和人口数量不匹配"   
China_Data = {}   
for city, China_Pop in zip(China_City, China_Population):  
    China_Data[city] = China_Pop  
print(China_Data)

# Sort the UK and China populations
sorted_UK_Cities= sorted(UK_Data.items(), key=lambda item: item[1], reverse=True)    
print(sorted_UK_Cities)  
sorted_UK_data_dict = dict(sorted_UK_Cities)    
print(sorted_UK_data_dict)

sorted_China_Cities= sorted(China_Data.items(), key=lambda item: item[1], reverse=True)    
print(sorted_China_Cities)  
sorted_China_data_dict = dict(sorted_China_Cities)    
print(sorted_China_data_dict)



# 提取城市和人口数据用于绘图  
sorted_UK_cities, sorted_UK_pops = zip(*sorted_UK_Cities)  
sorted_China_cities, sorted_China_pops = zip(*sorted_China_Cities)  


# Create bar plot for UK cities
plt.figure(figsize=(10, 6)) 
plt.bar(sorted_UK_cities, sorted_UK_pops, color='blue') 
plt.xlabel('Cities')
plt.ylabel('Population')    
plt.title('Population of UK Cities')  
plt.xticks(rotation=45) 
plt.tight_layout() 



# Create bar plot for China cities
plt.figure(figsize=(10, 6)) 
plt.bar(sorted_China_cities, sorted_China_pops, color='red') 
plt.xlabel('Cities')
plt.ylabel('Population')    
plt.title('Population of China Cities')  
plt.xticks(rotation=45) 
plt.tight_layout()


# 显示图形  
plt.show()