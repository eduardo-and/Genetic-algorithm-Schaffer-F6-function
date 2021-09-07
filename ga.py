
from genetic_algorithm.main import genetic_algorithm_algorithm


# CONSTANTS
POP_SIZE = 300
NUM_GER = 100000000
BITS = 44
CROSSOVER_RATE = 0.65
MUTATION_RATE = 0.0015
ELITISM = True


params={"pop_size": 100,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": CROSSOVER_RATE,
        "mutation_rate": MUTATION_RATE,
        "elitism": ELITISM
        }
    
   

apt, generation,crom = genetic_algorithm_algorithm(params)

print("\n\nApt:"+ str(round(apt,6))+"\nGeração:"+str(generation)+"\ncrom:"+crom)
    
      
      
