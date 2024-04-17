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
  
# SIR model
for t in range(1, 1000):  
    new_infections = np.random.binomial(S[t-1], beta * I[t-1] / N)  
    new_recoveries = np.random.binomial(I[t-1], gamma)  
    S[t] = S[t-1] - new_infections  
    I[t] = I[t-1] + new_infections - new_recoveries  
    R[t] = R[t-1] + new_recoveries  
  
# plot the results
plt.plot(S, label='Susceptible')  
plt.plot(I, label='Infected')  
plt.plot(R, label='Recovered')  
plt.legend()  
plt.show()