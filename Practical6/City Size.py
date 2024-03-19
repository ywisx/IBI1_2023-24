import numpy as np
import matplotlib.pyplot as plt

UK_City=["Edinburgh","Glasgow","Stirling","London"]
China_City=["Haining","Hangzhou","Shanghai","Beijing"]
UK_Population=[0.56,0.62,0.04,9.7]
China_Population=[0.58,8.4,29.9,22.2]

UK_Sort=sorted(UK_Population)
China_Sort=sorted(China_Population)
print("Sorted UK City Populations (millions):", UK_Sort)  
print("Sorted China City Populations (millions):", China_Sort)

plt.figure()
plt.bar(UK_City,UK_Population)
plt.title("UK City Sizes")
plt.xlabel("Cities")
plt.ylabel("Population(millions)")

plt.show()

plt.clf()