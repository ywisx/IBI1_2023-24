# import our base file
import SIR

# https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np  
# https://matplotlib.org/stable/api/index.html
import matplotlib.pyplot as plt

  
# from 0% to 100% of vaccination rates
vaccination_rates = [0,10,20,30,40,50,60,70,80,90,100]
# vaccination_rates = [10,50,80]        #used for test only


if __name__=='__main__':
    # plot the results
    plt.title("SIR model with different vaccination rates")
    plt.xlabel("Time")
    plt.ylabel("number of people")

    for rate in vaccination_rates:
        S, I, R = SIR.initData()
        for t in range(1, SIR.loopTimes):
            SIR.sirModelLoop(S, I, R, t, rate)

        #save it and start new plot data with only "infected" array
        label = "%d%%" % rate
        plt.plot(I, label=label)
        
    plt.legend()
    plt.show()