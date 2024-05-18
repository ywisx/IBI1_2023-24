# https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np  
# https://matplotlib.org/stable/api/index.html
import matplotlib.pyplot as plt


  
SIZE = 100    
# For this exercise, we will loop just through 100 time points.
LoopTimes = 100
beta = 0.3  
gamma = 0.05  

def showPlot(p, time):
    plt.figure ( figsize =(6 ,4) , dpi=150)
    title = "Times:%d" % time
    plt.title(title)
    
    #change all value from 2(recovered) to 0 for plot
    arr = np.where(p == 2, 0, p)

    # Colormap viridis is not recognized, so replace it
    plt.imshow(arr, cmap='hot' , interpolation='nearest')
    plt.show()
    

  
#Initialize the population  
 # 1 for infected, 0 for susceptible  , 2 for recovered
population = np.zeros((SIZE, SIZE))  
outbreak = np.random.choice(range(SIZE) ,2)
population[outbreak[0], outbreak[1]] = 1


# 1 2 3
# 4 x 6  <---  x means current infected people
# 7 8 9 
# create a row/column index offset table
neighborsOffset = [
    [ -1, -1], [-1, 0], [-1, 1],
    [0, -1],            [0, 1],
    [1, -1],   [1, 0],  [1, 1],
]

# choose a random neighbors position
def randomOffset():
    outbreak = np.random.randint(0, high=8)
    xindex = neighborsOffset[outbreak][0]
    yindex = neighborsOffset[outbreak][1]
    return xindex, yindex

def timeLoop(t):
    # oldICount = np.count_nonzero(np.where(population == 1, population, 0))
    oldICount = np.count_nonzero(population == 1)
    
    reduceICount = 0    # how many people recovered
    addedICount = 0 # how many people injected
    
    for x in range(0, SIZE):
        for y in range(0, SIZE):
            status = population[x, y]
            if status == 1:
                # for each "injected" => "recovered", check the value is 1, call random choice, and set it to 2 if TRUE
                arr = np.random.choice([True,False], 1, p=[gamma, 1-gamma])
                if arr[0]:
                     ### logic for "recovered", no need care about neighbours ###
                    population[x,y] = 2 # set already recovered
                    reduceICount += 1
            
            if status == 0: # 0 is susceptible
                arr = np.random.choice([True,False], 1, p=[beta, 1-beta])
                if arr[0]:
                    #  At each time point, an infected individual can infect any of its 8 neighbours with infection probability beta.
                    offset = randomOffset()
                    xindex = x + offset[0]
                    yindex = y + offset[1]
                    if xindex >= 0 and xindex < SIZE and yindex >=0 and yindex < SIZE:
                        if population[xindex, yindex] == 0:
                            # set a special value so no infect others in this loop
                            # later will change 99 to 1
                            population[xindex, yindex] = 99
                            addedICount += 1

    # replace temp 99 to 1
    # refer to https://www.statology.org/numpy-replace/
    population[population == 99] = 1

    newICount = np.count_nonzero(population == 1)
    print('#%d: infected %d=>%d  +%d -%d' % (t+1, oldICount, newICount, addedICount, reduceICount))
    
if __name__=='__main__':
    for t in range(LoopTimes):  
        timeLoop(t)

    # show the final array result as well
    s = np.count_nonzero(population==0)
    i = np.count_nonzero(population==1)
    r = np.count_nonzero(population==2)
    assert(s+i+r == SIZE*SIZE)
    print("\nTotal times:%d, susceptible:%d infected:%d recovered:%d\n" % (LoopTimes, s, i,r))
    print(population)
        
    # show final plot
    showPlot(population, LoopTimes)
