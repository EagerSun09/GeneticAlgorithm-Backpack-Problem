Course:	     CS-131-Artificial Intelligence
Assignment:  Genetic Algorithm
Name: 	     Yige Sun

I assume:
	i. The position of pancakes is 1 indexed.(The first position is 1.)

*******************************IMPORTANT NOTE*************************************
To try different weights or valuesof boxes, modify weight array and value array in Genetic class
Besides, if you want to try different number of generation, number of population and mutation, modify the number
at 193rd line when calling Genetic funtion. You should modify by the rule: 
		g=Genetic(number of generation, number of population, mutation)
****************************************************************************************
1. To define this problem as a genetic algorithm, chromosome represents the potential box selections to be placed 
in the bag. The problem begins starts with an array of box weights and an array of corrseponding values. A number
of chromosomes, which is the initial(random) population) are randomly generated to start the algorithm. The fitness
function that evaluates individuals is defined as the sum of values of boxes in individual's chromosome(If the sum of
weights of these boxes does not exceed the limit). If the sum of weights exceeds the limit of bag, the fitness will be 0.
At each step of algorithm, half of the population which has better fitness will remain and we will cull another half of 
population which has lower fitness. The mutation and crossover functions are executed on the fit individuals in the
population to generate next generation. The best individual at each step is the individual with the best fitness(i.e. the 
largest sum of values of boxes).

2. Provide genome for the problem
A chromosome is represented as an array. A 1 in that array means the box at that position is selected to be placed 
in the bag and a 0 means that box will not be selected.

3. To define all fringe operations, we need to define mutation and crossover.
	i. Mutation: select one cell of the chromosome and change its value.
	    eg. if the chromosome is 111 and we select position 3, after mutation, the chromosome will be 110.
	          if the chromosome is 111 and we select position 2,3. After mutation, we will get 100.
               ii. Crossover: it takes two individuals and produce a new one that has elements of each
	    eg. if there are 2 individuals 1100 and 0011, if we do crossover at 2nd position, we will get 1111 and 0000

4. Cull population by 50%
The culling process happens by sorting the current population according to fitness value (where fitness value is the 
sum of the values of the boxes, for any given selection of boxes). The half of the population with the highest fitness 
values remain, and another half of the population with the lower fitness values will be removed. 