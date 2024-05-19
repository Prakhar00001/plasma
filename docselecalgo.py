import random
import operator

def genetic_algorithm(population, fitness_function):
  best_individual = max(population, key=fitness_function)
  best_fitness = fitness_function(best_individual)
  while True:
    new_population = []
    for i in range(len(population)):
      parent1 = random.choice(population)
      parent2 = random.choice(population)
      child = crossover(parent1, parent2)
      mutation(child)
      new_population.append(child)
    population = new_population
    new_best_individual = max(population, key=fitness_function)
    new_best_fitness = fitness_function(new_best_individual)
    if new_best_fitness > best_fitness:
      best_individual = new_best_individual
      best_fitness = new_best_fitness
    else:
      break
  return best_individual

def crossover(parent1, parent2):
  # Perform crossover operation to generate a new individual
  # Example: Swap the middle part of the parent chromosomes
  mid = len(parent1) // 2
  child = parent1[:mid] + parent2[mid:]
  return child

def mutation(individual):
  # Perform mutation operation to generate a new individual
  # Example: Swap a random gene with another random gene
  gene1, gene2 = random.sample(range(len(individual)), 2)
  individual[gene1], individual[gene2] = individual[gene2], individual[gene1]

def fitness_function(individual):
  # Evaluate the fitness of the individual
  # Example: Count the number of specialists in the individual
  specialties = set([doctor.specialty for doctor in individual])
  return len(specialties)

# Example usage
doctors = [...]  # List of doctors
population = [...]  # List of individuals (lists of doctors)
best_individual = genetic_algorithm(population, fitness_function)