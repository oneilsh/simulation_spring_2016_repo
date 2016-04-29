import sys # we'll want to use sys.stdout.write()

class Individual:
    def __init__(self, coins_list, target):
        self.num_coins = len(coins_list)
        self.coins_list = coins_list
        self.target = target
        
        self.genotype = list()
        for i in range(0, self.num_coins):
            if random(0, 1) < 0.5:
                self.genotype.append(0)
            else:
                self.genotype.append(1)
                
                
    def __cmp__(self, other):
        if self.fitness() < other.fitness():
            return -1
        elif self.fitness() > other.fitness():
            return 1
        return 0
                
    def debug_print(self):
        for allele in self.genotype:
            sys.stdout.write(allele)
        sys.stdout.write("\n")
        
        
    def mate_with(self, mate):
        offspring = Individual(self.coins_list, self.target)
        
        crossover = int(random(0,self.num_coins))
        for i in range(0, crossover):
            offspring.genotype[i] = self.genotype[i]
        for i in range(crossover, len(self.genotype)):
            offspring.genotype[i] = mate.genotype[i]
            
        return offspring
    
    def fitness(self):
        sum = 0.0
        for i in range(0, self.num_coins):
            sum = sum + self.coins_list[i] * self.genotype[i]
            
        return abs(sum - self.target)
    
    
    def mutate(self):
        randindex = int(random(0, len(self.genotype)))
        if self.genotype[randindex] == 0:
            self.genotype[randindex] = 1
        else:
            self.genotype[randindex] = 0