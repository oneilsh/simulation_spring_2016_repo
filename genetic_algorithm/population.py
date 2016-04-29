from individual import Individual
import sys
import random as  randommodule # import the random module
                              # but call it randommodule so it doesn't
                              # conflict with the random() function
                              
                              
class Population:
    def __init__(self, popsize, coins_list, target):
        self.popsize = popsize
        self.num_coins = len(coins_list)
        self.coins_list = coins_list
        self.target = target
        
        self.individuals = list()
        for i in range(0, self.popsize):
            newind = Individual(self.coins_list, self.target)
            self.individuals.append(newind)
            
    def random_mate(self):
        for i in range(0, int(self.popsize/4.0)):
            pair = randommodule.sample(self.individuals, 2)
            offspring = pair[0].mate_with(pair[1])
            if random(0,1) < 0.1:
                offspring.mutate()
                
            self.individuals.append(offspring)
            
    
    def individual_fitness(self, ind):
        return ind.fitness()
    
    
    def cull(self):
        self.individuals.sort(key = self.individual_fitness)
        self.individuals.sort()
        self.individuals = self.individuals[0:self.popsize]
        
    
    def print_summary(self):
        fitnesses = list()
        sum = 0.0
        for ind in self.individuals:
            fitnesses.append(ind.fitness())
            sum = sum + ind.fitness()
            
        meanfit = sum/len(fitnesses)
        fitnesses.sort()
        medianfit = fitnesses[int(len(fitnesses)/2)]
        minfit = fitnesses[0]
        maxfit = fitnesses[len(fitnesses) - 1]
        
        print(" ")
        print(str(minfit) + " " + str(medianfit) + " " + str(meanfit) + " " + str(maxfit))
        self.individuals.sort(key = self.individual_fitness)
        self.individuals[0].debug_print()