import random

N = 8
POP_SIZE = 100
MAX_GEN = 1000
MUTATE_CHANCE = 0.1

def random_board(): return [random.randint(0, N - 1) for _ in range(N)]

def fitness(board):
    conflicts = sum(
        board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j)
        for i in range(N) for j in range(i + 1, N)
    )
    return -conflicts

def crossover(p1, p2):
    point = random.randint(0, N - 1)
    return p1[:point] + p2[point:]

def mutate(board):
    if random.random() < MUTATE_CHANCE:
        board[random.randint(0, N - 1)] = random.randint(0, N - 1)
    return board

def solve():
    population = [random_board() for _ in range(POP_SIZE)]
    for gen in range(MAX_GEN):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == 0:
            print(f" Found at generation {gen}: {population[0]}")
            return population[0]
        next_gen = []
        for _ in range(POP_SIZE):
            p1, p2 = random.choices(population[:50], k=2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)
        population = next_gen
    print("No solution found.")
    return None

solve()
