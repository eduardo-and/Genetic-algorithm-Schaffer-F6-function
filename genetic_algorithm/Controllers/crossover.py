import random


class Crossover():
    def __init__(self, population, rate, pop_size, bits):
        self.rate = rate
        self.pop_size = pop_size
        self.bits = bits
        self.population = population
        self.new_population = []

    def generate(self):
        i = 0
        while i < ((self.pop_size-1)+(self.pop_size%2)):
            rand = round(random.uniform(0.00, 1), 3)
            if(rand < self.rate):
                try:
                    self.cross(self.population[i], self.population[i+1])
                except:
                    self.cross(self.population[i], self.population[i-1])
            else:
                self.new_population.append(self.population[i])
                try:
                    self.new_population.append(self.population[i+1])
                except:
                    break
            i += 2
       

        return self.new_population

    def cross(self, x, y):
        rand = random.randint(1, self.bits-2)
        son1 = x[:rand] + y[rand:]
        son2 = x[rand:] + y[:rand]

        self.new_population.append(son1)
        self.new_population.append(son2)
