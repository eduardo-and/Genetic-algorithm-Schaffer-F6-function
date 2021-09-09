
from genetic_algorithm.Models.population import *
from genetic_algorithm.Controllers.aptitude import *
from genetic_algorithm.Controllers.roulette_selection import *
from genetic_algorithm.Controllers.crossover import *
from genetic_algorithm.Controllers.mutation import *
from genetic_algorithm.Controllers.elitism import *
from genetic_algorithm.Controllers.find_solution import *
import random
import numpy as np
import matplotlib.pyplot as plt



def genetic_algorithm_algorithm(params):

    # generate random population
    random_chromosomes = [[random.randint(0, 1) for i in range(0, params["bits"])] for i in range(0, params["pop_size"])]
    # Slide example
    random_chromosomes[0] = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
                       0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
    
    max_aptitude = []
    # Instace of model Population
    current_population = Population(
        random_chromosomes, params["pop_size"], params["bits"],Aptitude(random_chromosomes,params["pop_size"],params["bits"]).calculate())

    for i in range(0, params["num_ger"]):
        # print("\nGeneration: "+ str(i) +"  Highest aptitude: " + str(current_population.greater_aptitude())," Aptitude Mean: "+str(float(current_population.sumOfAptitude()/params["pop_size"]))+"\n"+str(current_population.greater_aptitude_chromosome()))
        # check if you found the solution
        max_aptitude.append(current_population.greater_aptitude())
        if(FindSolution(current_population).verify()):
            break

        # Roulette Selection
        selected_population = RoletteSelection(current_population).selection()

        # Crossover
        cross_population = Crossover(
            selected_population, params["crossover_rate"], params["pop_size"], params["bits"]).generate()

        # Mutation
        mutated_population = Mutation(
            cross_population, params["bits"], params["mutation_rate"]).mutate()

        # Current population to Parents population
        parents_population = current_population
        # Sons population going to current population
        current_population = Population(
            mutated_population, params["pop_size"], params["bits"],Aptitude(mutated_population,params["pop_size"],params["bits"]).calculate() )
        
        # print(max(parents_population.aptitude))
        # Check if Elitism is active, if it has, apply
        if(params["elitism"]):
            current_population,index = Elitism(current_population, parents_population).apply()
                        
            

    # At the end of generations, takes the node with the highest aptitude from the list of aptitudes and returns
    
    
    #Return highest aptitude and average aptitude
    return float(current_population.greater_aptitude()), str(i), str(current_population.greater_aptitude_chromosome()),max_aptitude