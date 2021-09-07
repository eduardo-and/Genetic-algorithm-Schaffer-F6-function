from genetic_algorithm.Controllers.aptitude import Aptitude


class FindSolution:
    def __init__(self, population):
        self.population = population
    
    def verify(self):
        aptitude = self.population.aptitude
        for index,node in enumerate(aptitude):
            if(round(node, 6) == 1.0):
                return True
            
        return False    