import random

class RoletteSelection:
    
    def __init__(self,population):
        self.population = population
        self.new_population = []
    
    def  selection(self):
        total = self.population.sumOfAptitude()
        sum_=0
        aptitude = self.population.aptitude
        
        for j in range(0,len(self.population.chromosomes)):
            rand = random.uniform(0,total)
            for i,apt in enumerate(aptitude): 
              sum_+=apt
              if(sum_>=rand):
                  self.new_population.append(self.population.chromosomes[i])
                  sum_=0
                  break
              
        return self.new_population