import numpy as np


class Aptitude:

    def __init__(self, population, pop_size, bits):
        self.population = population
        self.pop_size = pop_size
        self.bits = bits
        # half of bits
        self.half = int(bits/2)
        self.aux_number =200/(2**22-1)
        

    def calculate(self):
        aptitude = []
        for i in range(0, self.pop_size):
            node = self.population[i]                   
            x, y = self.slice_convert(node)            
            x, y = self.decode(x, y)            
            res = self.f6(x, y)            
            aptitude.append(res)
                       
        return aptitude
    
    def slice_convert(self, pop):

        # slice the list
        x = pop[:self.half]
        y = pop[self.half:]

        # convert integer to char
        x_char = [str(x) for x in x]
        y_char = [str(y) for y in y]

        #   Convert to integer base 10
        x = ""
        y = ""
        x = int(x.join(x_char), 2)
        y = int(y.join(y_char), 2)

        return x, y

    def decode(self, x, y):

        x = (x*self.aux_number)+(-100)
        y = (y*self.aux_number)+(-100)
        return x, y

    def f6(self, x, y):
        temp = x**2 + y**2
        res = 0.5 - ((np.sin(np.sqrt(temp))**2-0.5) / (1+(0.001*temp))**2)
        return res
