import os  
import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np  

os.chdir("/Users/zhuqin/Desktop/academic/IBI/Practical 7")   
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")  
print(dalys_data.iloc[0:110:10, 3])  
  
# Filtering DALYs in Afghanistan using Boolean lists  
afghanistan_bool_list = [country == 'Afghanistan' for country in dalys_data.iloc[:, 0]]  
afghanistan_dalys = dalys_data.loc[afghanistan_bool_list, "DALYs"]  
print(afghanistan_dalys)  
  
# Create a subset of China data  
china_bool_list = [country == 'China' for country in dalys_data.iloc[:, 0]]  
china_data = dalys_data.loc[china_bool_list, :]  
  
# Calculate average DALYs in China  
mean_china_DALYs = np.mean(china_data['DALYs'])  
print('average DALYs in China:', mean_china_DALYs)  
  
# Mapping DALYs over time in China  
plt.figure()  
plt.plot(china_data['Year'], china_data['DALYs'], 'b+')  
plt.xticks(china_data['Year'], rotation=-90)  
plt.title('DALYs over time in China')  
plt.show()  
plt.clf()  
  
# Box plots of DALYs by country for 2019  
year_2019_bool_list = [year == 2019 for year in dalys_data.iloc[:, 2]]  
data_2019 = dalys_data.loc[year_2019_bool_list, :]  
plt.boxplot(data_2019['DALYs'])  
plt.title('DALYs by country for 2019')  
plt.show()  
plt.clf()
