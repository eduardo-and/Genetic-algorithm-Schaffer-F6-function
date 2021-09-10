
from genetic_algorithm.main import genetic_algorithm_algorithm
import matplotlib.pyplot as plt

# CONSTANTS
POP_SIZE = 200
NUM_GER = 500
BITS = 44
CROSSOVER_RATE = 0.65
MUTATION_RATE = 0.0015
ELITISM = True


    
par = [
       {0"pop_size": 200,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": 0.60,
        "mutation_rate": 0.0015,
        "elitism": ELITISM},
       {"pop_size": 200,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": 0.70,
        "mutation_rate": 0.0015,
        "elitism": ELITISM},
       {"pop_size": 200,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": 0.75,
        "mutation_rate": 0.0015,
        "elitism": ELITISM},
       {"pop_size": 200,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": 0.55,
        "mutation_rate": 0.0015,
        "elitism": ELITISM}]   





y = [0,0,0,0]

for j in range(0,4):
    params_ = par[j];
    for i in range(0,1000):
        apt, generation,crom,max = genetic_algorithm_algorithm(params_)
        if(apt==1.0):    
            y[j] += 1
    

names = ["Mut: 0.0015 cros: 0.60","Mut: 0.0015 cros: 0.70", "Mut: 0.0015 cros: 0.75","Mut: 0.0015 cros: 0.55"]

y[0] = y[0]/1000
y[1] = y[1]/1000
y[2] = y[2]/1000
y[3] = y[3]/1000

plt.title("Eficácia média em 1000 execuções")
      

plt.bar(names, y)
plt.savefig("teste.png")