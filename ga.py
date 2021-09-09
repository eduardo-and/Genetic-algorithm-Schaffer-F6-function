
from genetic_algorithm.main import genetic_algorithm_algorithm
import matplotlib.pyplot as plt

# CONSTANTS
POP_SIZE = 100
NUM_GER = 1000
BITS = 44
CROSSOVER_RATE = 0.65
MUTATION_RATE = 0.0015
ELITISM = True


params={"pop_size": POP_SIZE,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": CROSSOVER_RATE,
        "mutation_rate": MUTATION_RATE,
        "elitism": ELITISM
        }
    
   

apt, generation,crom,max = genetic_algorithm_algorithm(params)

print("\n\nApt:"+ str(round(apt,6))+"\nGeração:"+str(generation)+"\ncrom:"+crom+"\n\n")
print(params)

y = [x for x in range(0,int(generation)+1)]
plt.plot(y,max)
plt.axis([0, int(generation)+1, 0, 1])
plt.ylabel('some numbers')
plt.show()      
      
# plt.bar(names, values)