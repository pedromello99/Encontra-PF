from itertools import combinations
import csv

def load_data(filepath):
    """Carrega os dados de um arquivo CSV."""
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        return [float(row[0]) for row in reader]

def find_combinations(X, Y):
    """Encontra combinações de valores em X que somam Y."""
    for r in range(1, len(X) + 1):
        for combo in combinations(X, r):
            if round(sum(combo), 2) == Y:
                return list(combo)
    return None

def main():
    filepath = 'data/example_input.csv'
    Y = 409182.76
    X = load_data(filepath)
    
    result = find_combinations(X, Y)
    if result:
        print(f"Combinação encontrada: {result}")
    else:
        print("Nenhuma combinação exata encontrada.")

if __name__ == "__main__":
    main()
