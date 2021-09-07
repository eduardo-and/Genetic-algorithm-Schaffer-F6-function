import random
class Mutation:
    def __init__(self,population,bits,rate):
        self.population= population
        self.bits = bits
        self.rate = rate
        self.mutacoes= 0
    
    def mutate(self):

        for index,i in enumerate(self.population):
            for x,j in enumerate(i):
                rand = round(random.uniform(0,1),3)
          
                if(rand<self.rate):
                    if(j==0):i[x]=1
                    else:i[x]=0
                    self.mutacoes = self.mutacoes+1                    
        # print(mutacoes)
        return self.population
        
                
        
        