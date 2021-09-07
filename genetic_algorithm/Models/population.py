

class Population:

    def __init__(self, population,pop_size,bits,aptitude = []):
        self.chromosomes = population
        self.pop_size = pop_size
        self.bits = bits
        self.aptitude = aptitude

    def setchromosomes(self, chromosomes):
        self.chromosomes = chromosomes

    def setAptitude(self, aptitude):
        self.aptitude = aptitude

    def sumOfAptitude(self):
        sum_= sum([x for x in self.aptitude])
        return sum_
    
    def setAptitude(self,aptitude):
        self.aptitude = aptitude
        
    def greater_aptitude(self):
        return max(self.aptitude)
    
    def greater_aptitude_chromosome(self):
        return self.chromosomes[self.aptitude.index(max(self.aptitude))]