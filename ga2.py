
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
       {"pop_size": 100,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": 0.65,
        "mutation_rate": 0.008,
        "elitism": ELITISM},
       {"pop_size": 200,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": CROSSOVER_RATE,
        "mutation_rate": 0.005,
        "elitism": True},
       {"pop_size": 200,
        "num_ger": NUM_GER,
        "bits": BITS,
        "crossover_rate": 0.65,
        "mutation_rate": 0.0015,
        "elitism": ELITISM}]   



y = [0,0,0]

for j in range(0,3):
    params_ = par[j];
    for i in range(0,1000):
        apt, generation,crom,max = genetic_algorithm_algorithm(params_)
        if(apt==1.0):    
            y[j] += 1
    

names = ["Mutation: 0.008 Pop:100","Mutation: 0.005 Pop:200", "Mutation: 0.0015 Pop:200"]

y[0] = y[0]/1000
y[1] = y[1]/1000
y[2] = y[2]/1000

plt.title("Eficácia média em 1000 execuções")
      
plt.savefig("teste.png")
plt.bar(names, y)