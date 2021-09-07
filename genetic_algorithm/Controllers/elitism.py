from genetic_algorithm.Controllers.aptitude import Aptitude


class Elitism:
    def __init__(self,population,oldPopulation):
        self.pop = population
        self.oldPop = oldPopulation
        
    
    def apply(self):
        
        less_aptitude = min(self.pop.aptitude)
        bigger_aptitude = max(self.oldPop.aptitude)
        
                         
        less_index = self.pop.aptitude.index(less_aptitude)
        bigger_index = self.oldPop.aptitude.index(bigger_aptitude)
         
        self.pop.chromosomes[less_index]= self.oldPop.chromosomes[bigger_index]
        self.pop.aptitude[less_index] =  self.oldPop.aptitude[bigger_index]
                
        return self.pop,less_index