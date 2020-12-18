import numpy as np
import random as rn
import math

#objective function
def f(x):
    x1 = x[0]
    x2 = x[1]
    obj = ((math.sin((x1-x2/8)**2))+(math.sin((x2+x1/8)**2)))/(((((x1-8.6998)**2)+((x2-6.7665)**2))**0.5)+1)
    return obj


print("T   Solution   delta_f   Move?")


def simulated_annealing():
#Start location
    initial_x = [rn.randint(0,64), rn.randint(0,64)]
    initial_temp = 70
    


    current_temp = initial_temp
    current_state = f(initial_x)


    while(current_temp > 0):
        
        next_state = get_neighbor()
        move = False
        
        
        delta_f = next_state - current_state

        if delta_f > 0:
            current_state = next_state
            move = True

        else:
            if rn.uniform(0, 1) < acceptance_probability(delta_f,current_temp):
                current_state = next_state
                move = True
        
        print(current_temp, current_state, delta_f, move,delta_f + current_state,sep='      ')            
        current_temp = cooling(current_temp)
        
    
    
    return current_state

    
def cooling(current_temp):   
    new_temp = rn.randint(current_temp-10 if current_temp-10 > 0 else 0, current_temp-3 if current_temp -3 > 0 else 0) 
    return new_temp

def acceptance_probability(delta_f,current_temp):
    return math.exp(delta_f/current_temp) 
    
    

def get_neighbor():
    new_x = [rn.randint(0,64), rn.randint(0,64)]
    new_state = f(new_x)
    return new_state 
    
    
    
print(simulated_annealing())
