# Initialize the array 
import numpy as np  
import matplotlib.pyplot as plt  
  
# Initialization parameters  
N = 10000  
I0 = 1  
S0 = N - I0  
R0 = 0  
beta = 0.3  
gamma = 0.05  
  
# Initialize the array  
S = np.zeros(1000)  
I = np.zeros(1000)  
R = np.zeros(1000)  
S[0] = S0  
I[0] = I0  
R[0] = R0  

vaccination_rate = 0.1   
S0_vaccinated = int(S0 * vaccination_rate)  
S0_non_vaccinated = S0 - S0_vaccinated  
  
  
S_vaccinated = np.zeros(1000)  
S_non_vaccinated = np.zeros(1000)  
S_vaccinated[0] = S0_vaccinated  
S_non_vaccinated[0] = S0_non_vaccinated  
I = np.zeros(1000)  
I[0] = I0  
R = np.zeros(1000)  


# SIR model updated to account for vaccinations  
for t in range(1, 1000):  
    
    new_infections = np.random.binomial(S_non_vaccinated[t-1], beta * I[t-1] / N)  
    new_recoveries = np.random.binomial(I[t-1], gamma)  
    S_non_vaccinated[t] = S_non_vaccinated[t-1] - new_infections  
    S_vaccinated[t] = S_vaccinated[t-1]    
    I[t] = I[t-1] + new_infections - new_recoveries  
    R[t] = R[t-1] + new_recoveries  
  
# plot the results
plt.plot(S_vaccinated + S_non_vaccinated, label='Susceptible')  
plt.plot(I, label='Infected')  
plt.plot(R, label='Recovered')  
plt.legend()  
plt.show()