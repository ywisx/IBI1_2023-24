 # import necessary libraries  
import numpy as np  
import matplotlib.pyplot as plt  
  
# Define initial parameters  
N = 10000  
I0 = 1  
R0 = 0  
S0 = N - I0 - R0  
beta = 0.3  
gamma = 0.05  
  
# Initialize arrays 
T = 1000  
S = [S0] * T  
I = [I0] * T  
R = [R0] * T  
  
# Time loop  
for t in range(T - 1): 
    # Calculate new infections and recoveries  
    new_infections = np.random.binomial(S[t], beta * I[t] / N)  
    new_recoveries = np.random.binomial(I[t], gamma)  
      
    # Update the states  
    S[t + 1] = S[t] - new_infections  
    I[t + 1] = I[t] + new_infections - new_recoveries  
    R[t + 1] = R[t] + new_recoveries  
      
    # Ensure that the numbers are non-negative and total population is constant  
    S[t + 1] = max(S[t + 1], 0)  
    I[t + 1] = max(I[t + 1], 0)  
    R[t + 1] = N - S[t + 1] - I[t + 1]  
  
# Plot the results  
plt.plot(range(T), S, label='Susceptible')  
plt.plot(range(T), I, label='Infected')  
plt.plot(range(T), R, label='Recovered')  
  
plt.xlabel('Time')  
plt.ylabel('Number of individuals')  
plt.title('SIR Model Over Time')  
plt.legend()  
  
plt.show()
