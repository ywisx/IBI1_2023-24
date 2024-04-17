# Initialize the array 
import numpy as np  
import matplotlib.pyplot as plt  
  
N = 100    
beta = 0.3  
gamma = 0.1  
initial_infected = 10    
timesteps = 100   
  
#Initialize the grid  
grid = np.zeros((N, N), dtype=int)  
initial_infections = np.random.choice(N*N, initial_infected, replace=False)  
grid.ravel()[initial_infections] = 1  # 1 for infected, 0 for susceptible  
  
# Modeling disease transmission  
for t in range(timesteps):  
    new_grid = grid.copy()  
    for i in range(N):  
        for j in range(N):  
            if grid[i, j] == 1:  
                if np.random.rand() < gamma:    
                    new_grid[i, j] = 2  
            elif grid[i, j] == 0:  

                infected_neighbors = (grid[i-1:i+2, j-1:j+2] == 1).sum() - grid[i, j]  
                if infected_neighbors > 0 and np.random.rand() < beta * infected_neighbors:  
                    new_grid[i, j] = 1    
    grid = new_grid  
  
#plot the results  
plt.imshow(grid, cmap='hot', interpolation='nearest')  
plt.colorbar()  
plt.title('Final State')  
plt.show()
