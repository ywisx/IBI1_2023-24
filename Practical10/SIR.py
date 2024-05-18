# https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np  
# https://matplotlib.org/stable/api/index.html
import matplotlib.pyplot as plt  

  
# init const parameters   
population = 10000  
beta = 0.3  
gamma = 0.05  

loopTimes = 1000


# init test data
def initData():
    S = np.zeros(loopTimes)  
    I = np.zeros(loopTimes)  
    R = np.zeros(loopTimes)  
    S[0] = population - I[0]
    return S, I, R


# SIR model loop
def sirModelLoop(S, I, R, index, vaccination_rate):  
     # account for this by multiplying beta by the proportion of infected people in the population
    p0 =  (population - I[index - 1]) / population * beta 
    p0 *= (1 - (vaccination_rate / 100.0))
    
    # print(vaccination_rate, p0)

    # repeat multiple times, with probability
    arr = np.random.choice([1,0], S[index-1],p=[p0, 1-p0])
    # 1 means "will be infected", 0 means "No", count the "infected" number
    new_infections = np.count_nonzero(arr)

    # same logic for "recovered"
    arr = np.random.choice([1,0], I[index-1], p=[gamma, 1-gamma])
    new_recoveries = np.count_nonzero(arr)
    
   
    # update for next loop
    S[index] = S[index - 1] - new_infections  
    I[index] = I[index - 1] + new_infections - new_recoveries  
    R[index] = R[index - 1] + new_recoveries
    print('#%d: vaccination %d%% infected %d=>%d  +%d -%d' % (index+1, vaccination_rate, I[index - 1], I[index], new_infections, new_recoveries))

  
if __name__=='__main__':
    S, I, R  = initData()
    for t in range(1, loopTimes):
        sirModelLoop(S, I, R, t, 0)

    # plot SIR modle results
    plt.figure( figsize =(6 ,4) , dpi=150)
    plt.title("SIR Model")
    plt.xlabel("Time")
    plt.ylabel("number of people")
    
    plt.plot(S, label='Susceptible')  
    plt.plot(I, label='Infected')  
    plt.plot(R, label='Recovered')  
    plt.legend()  
    plt.show()

